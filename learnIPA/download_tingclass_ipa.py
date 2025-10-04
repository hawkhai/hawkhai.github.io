import os
import re
import json
import time
import errno
from pathlib import Path
from urllib.parse import urljoin
from typing import Optional

import requests

IPA_PAGE = "https://ielts.biomooc.com/speaking/IPA.html"
MAPPING_FILE = r"D:\\kSource\\blog\\learnIPA\\phonetic_mapping_backup.json"
OUTPUT_DIR = Path(r"D:\\kSource\\blog\\learnIPA\\tingclass")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# Map the symbols as they appear on the biomooc/tingclass pages to the mapping file keys
SITE_TO_MAPPING = {
    # Long vowels (ASCII colon -> length mark)
    "i:": "iː",
    "ə:": "ɜː",
    "a:": "ɑː",
    "ɔ:": "ɔː",
    "u:": "uː",
    # Short vowels (site -> IPA used by mapping)
    "i": "ɪ",
    "u": "ʊ",
    "ɔ": "ɒ",  # site shows ɔ (short), mapping uses ɒ
    # Diphthongs
    "ei": "eɪ",
    "ai": "aɪ",
    "ɔi": "ɔɪ",
    "əu": "əʊ",
    "au": "aʊ",
    "iə": "ɪə",
    "εə": "eə",  # site uses Greek epsilon
    # Affricates and fricatives variants
    "t∫": "tʃ",
    "∫": "ʃ",
    # Everything identical maps to itself, handled later
}

# Fallback identicals that often appear as-is
IDENTICALS = set([
    "e", "æ", "ə", "ʌ", "p", "t", "k", "f", "θ", "s", "ʃ", "h",
    "v", "ð", "z", "ʒ", "r", "dʒ", "ts", "tr", "b", "d", "g",
    "dz", "dr", "m", "n", "ŋ", "l", "j", "w", "tʃ"
])

SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def ensure_dir(path: Path):
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def load_mapping(mapping_path: str):
    with open(mapping_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    phonetic_to_numeric = data.get("phonetic_to_numeric", {})
    return phonetic_to_numeric


def normalize_site_symbol(raw: str) -> str:
    s = raw.strip()
    # strip surrounding brackets like [i:], [ tʃ ] etc.
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1].strip()
    # unify spaces
    s = s.replace("\u00a0", " ").strip()
    # Apply explicit mapping first
    if s in SITE_TO_MAPPING:
        return SITE_TO_MAPPING[s]
    # If contains colon anywhere, convert ASCII colon to length mark
    if ":" in s:
        s = s.replace(":", "ː")
    # Replace Greek epsilon to latin e
    s = s.replace("ε", "e")
    # Replace legacy symbols to modern ones if present
    s = s.replace("∫", "ʃ")
    s = s.replace("t∫", "tʃ")
    return s


def fetch(url: str) -> str:
    resp = SESSION.get(url, timeout=20)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or resp.encoding

    return resp.text


def find_tingclass_links(html: str):
    # Capture: href to tingclass detail + inner text like [i:], [tʃ]
    # Updated pattern to match the actual HTML structure from the sample
    pattern = re.compile(r'<a[^>]+href="(http://www\.tingclass\.net/show-[^"]+)"[^>]*target="_blank">(\[[^\]]+\])</a>', re.I)
    links = []
    for m in pattern.finditer(html):
        href = m.group(1)
        label = m.group(2)  # Already includes brackets like [i:]
        links.append((label, href))
    
    # De-duplicate by href
    dedup = {}
    for label, href in links:
        dedup[href] = label
    return [(dedup[h], h) for h in dedup]

def extract_mp4_url(detail_html: str, base_url: str) -> Optional[str]:
    # Try <video src="...mp4">
    m = re.search(r"<video[^>]+src=['\"]([^'\"]+?\.mp4)['\"]", detail_html, re.I)
    if m:
        return urljoin(base_url, m.group(1))
    # Try <source src="...mp4">
    m = re.search(r"<source[^>]+src=['\"]([^'\"]+?\.mp4)['\"]", detail_html, re.I)
    if m:
        return urljoin(base_url, m.group(1))
    # Generic: any .mp4 in the HTML
    m = re.search(r"https?://[^\s'\"]+?\.mp4", detail_html, re.I)
    if m:
        return m.group(0)
    return None


def download_file(url: str, dest_path: Path, retries: int = 3):
    for attempt in range(1, retries + 1):
        try:
            with SESSION.get(url, stream=True, timeout=60) as r:
                r.raise_for_status()
                with open(dest_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            return
        except Exception as e:
            if attempt == retries:
                raise
            time.sleep(1.5 * attempt)


def main():
    ensure_dir(OUTPUT_DIR)
    mapping = load_mapping(MAPPING_FILE)

    print(f"Loaded {len(mapping)} mapping entries from {MAPPING_FILE}")

    print(f"Fetching index page: {IPA_PAGE}")
    index_html = fetch(IPA_PAGE)
    pairs = find_tingclass_links(index_html)

    if not pairs:
        print("No tingclass links found on the index page. Aborting.")
        return

    print(f"Found {len(pairs)} candidate links on index page.")

    success = 0
    skipped = 0
    failed_details = []
    skipped_details = []

    for raw_label, href in pairs:
        ipa = normalize_site_symbol(raw_label)
        # Allow identicals pass-through
        if ipa in IDENTICALS:
            norm = ipa
        else:
            norm = ipa
        code = mapping.get(norm)
        if code is None:
            # Some pages might list alternative forms; try a few fallbacks
            alt = None
            if norm == "eɪ":
                alt = "ei"
            elif norm == "aɪ":
                alt = "ai"
            elif norm == "ɔɪ":
                alt = "ɔi"
            elif norm == "əʊ":
                alt = "əu"
            elif norm == "aʊ":
                alt = "au"
            elif norm == "ɪə":
                alt = "iə"
            elif norm == "eə":
                alt = "εə"
            elif norm == "ʃ":
                alt = "∫"
            elif norm == "tʃ":
                alt = "t∫"
            if alt and mapping.get(alt):
                code = mapping[alt]
        if code is None:
            reason = f"No mapping code for '{raw_label}' -> '{norm}'"
            print(f"[SKIP] {reason}")
            skipped_details.append((raw_label, norm, href, reason))
            skipped += 1
            continue

        # Fetch detail page and extract mp4
        try:
            detail_html = fetch(href)
        except Exception as e:
            reason = f"Fetch detail failed: {e}"
            print(f"[ERROR] {reason}")
            failed_details.append((raw_label, norm, href, reason))
            skipped += 1
            continue

        mp4_url = extract_mp4_url(detail_html, href)
        if not mp4_url:
            reason = "No mp4 found in page"
            print(f"[SKIP] {reason} - {href}")
            skipped_details.append((raw_label, norm, href, reason))
            skipped += 1
            continue

        # Build filename - only use numeric code to avoid encoding issues
        filename = f"{code}.mp4"
        dest = OUTPUT_DIR / filename
        if dest.exists() and dest.stat().st_size > 0:
            print(f"[EXIST] {dest.name}")
            success += 1
            continue

        try:
            print(f"[GET ] {raw_label} -> {norm} ({code}) => {mp4_url}")
            download_file(mp4_url, dest)
            print(f"[SAVE] {dest}")
            success += 1
        except Exception as e:
            reason = f"Download failed: {e}"
            print(f"[FAIL] {raw_label} -> {norm} ({code}) from {mp4_url}: {e}")
            failed_details.append((raw_label, norm, href, reason))
            skipped += 1

    # Print detailed report
    print(f"\n=== DOWNLOAD REPORT ===")
    print(f"Total links found: {len(pairs)}")
    print(f"Successfully downloaded: {success}")
    print(f"Skipped/Failed: {skipped}")
    print(f"Files saved to: {OUTPUT_DIR}")
    
    if skipped_details:
        print(f"\n=== SKIPPED FILES ({len(skipped_details)}) ===")
        for raw_label, norm, href, reason in skipped_details:
            print(f"  {raw_label} -> {norm}: {reason}")
    
    if failed_details:
        print(f"\n=== FAILED FILES ({len(failed_details)}) ===")
        for raw_label, norm, href, reason in failed_details:
            print(f"  {raw_label} -> {norm}: {reason}")
    
    print(f"\n=== SUCCESS RATE ===")
    print(f"{success}/{len(pairs)} = {success/len(pairs)*100:.1f}%")


if __name__ == "__main__":
    main()
