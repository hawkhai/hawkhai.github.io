import os
import re
import json
import time
import errno
from pathlib import Path
from typing import Optional, Dict, List, Tuple

import requests

MAPPING_FILE = r"D:\kSource\blog\learnIPA\phonetic_mapping_backup.json"
OUTPUT_DIR = Path(r"D:\kSource\blog\learnIPA\xdf")
BASE_URL = "https://www.xdf.cn/zhuanti/bd-phonetic-alphabet-card/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# 从JS文件中提取的音标ID到文件名的映射
XDF_AUDIO_MAPPING = {
    # 元音 - 单元音 - 前元音
    "0-0-0-0": "496fa8c5b185e9d155d7.mp3",  # [i:]
    "0-0-0-1": "9eeb45ac15980f053465.mp3",  # [ɪ]
    "0-0-0-2": "51f575eab8eb20b5fbf7.mp3",  # [e]
    "0-0-0-3": "0d692636a009ea99b9f9.mp3",  # [æ]
    
    # 元音 - 单元音 - 中元音
    "0-0-1-0": "2b2c11bd1dcf81f786f0.mp3",  # [ɜ:]
    "0-0-1-1": "04c02a21344cc0750a68.mp3",  # [ə]
    "0-0-1-2": "1c0775f0ef22273a7e85.mp3",  # [ʌ]
    
    # 元音 - 单元音 - 后元音
    "0-0-2-0": "45f67d333cfcb525cd4f.mp3",  # [u:]
    "0-0-2-1": "ef8b714cea50701066b8.mp3",  # [ʊ]
    "0-0-2-2": "bdd75c97619e90b5035d.mp3",  # [ɔ:]
    "0-0-2-3": "9bf1a8bbcfc0c68ee326.mp3",  # [ɒ]
    "0-0-2-4": "db4b962669f0c8e54737.mp3",  # [ɑ:]
    
    # 元音 - 双元音 - 开合双元音
    "0-1-0-0": "28dc047b815750a6c5ee.mp3",  # [eɪ]
    "0-1-0-1": "a83bc6c3a61e526de4ba.mp3",  # [aɪ]
    "0-1-0-2": "c037f2e2fa30fc2711b8.mp3",  # [ɔɪ]
    "0-1-0-3": "8088e9346a7f75cb9b3c.mp3",  # [aʊ]
    "0-1-0-4": "eae06d0db4f09c8f142c.mp3",  # [əʊ]
    
    # 元音 - 双元音 - 集中双元音
    "0-1-1-0": "6ff61b12d4e985c668ac.mp3",  # [ɪə]
    "0-1-1-1": "f4eac5545f36dce272b8.mp3",  # [eə]
    "0-1-1-2": "1c01bd93c34338ca2081.mp3",  # [ʊə]
    
    # 辅音 - 清辅音 - 爆破音
    "1-0-0-0": "de1d50e7127182f7704d.mp3",  # [p]
    "1-0-0-1": "5df0fde0b4fd99cee219.mp3",  # [t]
    "1-0-0-2": "2d9c9b3d1ecdf33d659a.mp3",  # [k]
    
    # 辅音 - 清辅音 - 摩擦音
    "1-0-1-0": "a4209e9d9fd9709a1e76.mp3",  # [f]
    "1-0-1-1": "9b0599891bade0c04c46.mp3",  # [s]
    "1-0-1-2": "c4a898ad851940132475.mp3",  # [ʃ]
    "1-0-1-3": "d994b922bc7ec82646ff.mp3",  # [θ]
    "1-0-1-4": "fc7ee36388f605e0a8c6.mp3",  # [h]
    
    # 辅音 - 清辅音 - 破擦音
    "1-0-2-0": "a8bd1716350ce6be0735.mp3",  # [tʃ]
    "1-0-2-1": "4fad2aa8319f96b7034c.mp3",  # [tr]
    "1-0-2-2": "b854e5495600f691d169.mp3",  # [ts]
    
    # 辅音 - 浊辅音 - 爆破音
    "1-1-0-0": "f80e74ce936868ba6237.mp3",  # [b]
    "1-1-0-1": "9a351a93fddb04c95162.mp3",  # [d]
    "1-1-0-2": "9f1f33f7bd448e4b2262.mp3",  # [g]
    
    # 辅音 - 浊辅音 - 摩擦音
    "1-1-1-0": "1ee6a0a833eb5f5c40b4.mp3",  # [v]
    "1-1-1-1": "21d839e770c9a38de14a.mp3",  # [z]
    "1-1-1-2": "69df71ab3487efcb6bfa.mp3",  # [ʒ]
    "1-1-1-3": "ab9c619dfb987add2069.mp3",  # [ð]
    "1-1-1-4": "b6c52369def91ab36852.mp3",  # [r]
    
    # 辅音 - 浊辅音 - 破擦音
    "1-1-2-0": "70e57979284156031990.mp3",  # [dʒ]
    "1-1-2-1": "f981507e87b07895a224.mp3",  # [dr]
    "1-1-2-2": "a9879c494d9159bdd679.mp3",  # [dz]
    
    # 辅音 - 浊辅音 - 鼻音
    "1-1-3-0": "01ef4567a1aa014ae30a.mp3",  # [m]
    "1-1-3-1": "7f9f8679b25155de6b47.mp3",  # [n]
    "1-1-3-2": "9f10d5b95482af1e9815.mp3",  # [ŋ]
    
    # 辅音 - 浊辅音 - 舌侧音
    "1-1-4-0": "a4c2272a2e766194a4a1.mp3",  # [l] (注意：原文显示为[ǀ]，但应该是[l])
    
    # 辅音 - 浊辅音 - 半元音
    "1-1-5-0": "fe61e7decb7acb2e0d8b.mp3",  # [j]
    "1-1-5-1": "4e6d33cbf2ba6dfb91b7.mp3",  # [w]
}

# XDF网站的音标ID到IPA符号的映射
XDF_ID_TO_IPA = {
    # 元音 - 单元音 - 前元音
    "0-0-0-0": "iː",   # [i:]
    "0-0-0-1": "ɪ",    # [ɪ]
    "0-0-0-2": "e",    # [e]
    "0-0-0-3": "æ",    # [æ]
    
    # 元音 - 单元音 - 中元音
    "0-0-1-0": "ɜː",   # [ɜ:]
    "0-0-1-1": "ə",    # [ə]
    "0-0-1-2": "ʌ",    # [ʌ]
    
    # 元音 - 单元音 - 后元音
    "0-0-2-0": "uː",   # [u:]
    "0-0-2-1": "ʊ",    # [ʊ]
    "0-0-2-2": "ɔː",   # [ɔ:]
    "0-0-2-3": "ɒ",    # [ɒ]
    "0-0-2-4": "ɑː",   # [ɑ:]
    
    # 元音 - 双元音 - 开合双元音
    "0-1-0-0": "eɪ",   # [eɪ]
    "0-1-0-1": "aɪ",   # [aɪ]
    "0-1-0-2": "ɔɪ",   # [ɔɪ]
    "0-1-0-3": "aʊ",   # [aʊ]
    "0-1-0-4": "əʊ",   # [əʊ]
    
    # 元音 - 双元音 - 集中双元音
    "0-1-1-0": "ɪə",   # [ɪə]
    "0-1-1-1": "eə",   # [eə]
    "0-1-1-2": "ʊə",   # [ʊə]
    
    # 辅音 - 清辅音 - 爆破音
    "1-0-0-0": "p",    # [p]
    "1-0-0-1": "t",    # [t]
    "1-0-0-2": "k",    # [k]
    
    # 辅音 - 清辅音 - 摩擦音
    "1-0-1-0": "f",    # [f]
    "1-0-1-1": "s",    # [s]
    "1-0-1-2": "ʃ",    # [ʃ]
    "1-0-1-3": "θ",    # [θ]
    "1-0-1-4": "h",    # [h]
    
    # 辅音 - 清辅音 - 破擦音
    "1-0-2-0": "tʃ",   # [tʃ]
    "1-0-2-1": "tr",   # [tr]
    "1-0-2-2": "ts",   # [ts]
    
    # 辅音 - 浊辅音 - 爆破音
    "1-1-0-0": "b",    # [b]
    "1-1-0-1": "d",    # [d]
    "1-1-0-2": "g",    # [g]
    
    # 辅音 - 浊辅音 - 摩擦音
    "1-1-1-0": "v",    # [v]
    "1-1-1-1": "z",    # [z]
    "1-1-1-2": "ʒ",    # [ʒ]
    "1-1-1-3": "ð",    # [ð]
    "1-1-1-4": "r",    # [r]
    
    # 辅音 - 浊辅音 - 破擦音
    "1-1-2-0": "dʒ",   # [dʒ]
    "1-1-2-1": "dr",   # [dr]
    "1-1-2-2": "dz",   # [dz]
    
    # 辅音 - 浊辅音 - 鼻音
    "1-1-3-0": "m",    # [m]
    "1-1-3-1": "n",    # [n]
    "1-1-3-2": "ŋ",    # [ŋ]
    
    # 辅音 - 浊辅音 - 舌侧音
    "1-1-4-0": "l",    # [l]
    
    # 辅音 - 浊辅音 - 半元音
    "1-1-5-0": "j",    # [j]
    "1-1-5-1": "w",    # [w]
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def ensure_dir(path: Path):
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def load_mapping(mapping_path: str) -> Dict[str, str]:
    with open(mapping_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    phonetic_to_numeric = data.get("phonetic_to_numeric", {})
    return phonetic_to_numeric


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
    print(f"Found {len(XDF_AUDIO_MAPPING)} XDF audio files to download")
    
    success = 0
    skipped = 0
    failed_details = []
    skipped_details = []
    
    for xdf_id, filename in XDF_AUDIO_MAPPING.items():
        ipa_symbol = XDF_ID_TO_IPA.get(xdf_id)
        if not ipa_symbol:
            reason = f"No IPA symbol mapping for XDF ID: {xdf_id}"
            print(f"[SKIP] {reason}")
            skipped_details.append((xdf_id, filename, reason))
            skipped += 1
            continue
        
        # 查找本地映射中的数字编码
        numeric_code = mapping.get(ipa_symbol)
        if not numeric_code:
            # 尝试一些变体映射
            alt_mappings = {
                "ɜː": "ə:",
                "ɒ": "ɔ", 
                "ɪ": "i",
                "ʊ": "u",
                "eə": "εə",
                "ʃ": "∫",
                "tʃ": "t∫"
            }
            alt_symbol = alt_mappings.get(ipa_symbol)
            if alt_symbol:
                numeric_code = mapping.get(alt_symbol)
        
        if not numeric_code:
            reason = f"No numeric mapping for IPA symbol: {ipa_symbol}"
            print(f"[SKIP] {reason}")
            skipped_details.append((xdf_id, ipa_symbol, reason))
            skipped += 1
            continue
        
        # 构建下载URL和目标文件名
        audio_url = BASE_URL + filename
        dest_filename = f"{numeric_code}.mp3"
        dest_path = OUTPUT_DIR / dest_filename
        
        # 检查文件是否已存在
        if dest_path.exists() and dest_path.stat().st_size > 0:
            print(f"[EXIST] {dest_filename}")
            success += 1
            continue
        
        # 下载文件
        try:
            print(f"[GET ] {xdf_id} -> {numeric_code} => {audio_url}")
            download_file(audio_url, dest_path)
            print(f"[SAVE] {dest_filename} ({dest_path.stat().st_size} bytes)")
            success += 1
        except Exception as e:
            reason = f"Download failed: {e}"
            print(f"[FAIL] {xdf_id} -> {numeric_code}: {e}")
            failed_details.append((xdf_id, ipa_symbol, audio_url, reason))
            skipped += 1
    
    # 打印详细报告
    print(f"\n=== XDF DOWNLOAD REPORT ===")
    print(f"Total XDF audio files: {len(XDF_AUDIO_MAPPING)}")
    print(f"Successfully downloaded: {success}")
    print(f"Skipped/Failed: {skipped}")
    print(f"Files saved to: {OUTPUT_DIR}")
    
    if skipped_details:
        print(f"\n=== SKIPPED FILES ({len(skipped_details)}) ===")
        for item in skipped_details:
            if len(item) == 3:
                xdf_id, ipa_or_filename, reason = item
                print(f"  {xdf_id} -> {ipa_or_filename}: {reason}")
    
    if failed_details:
        print(f"\n=== FAILED FILES ({len(failed_details)}) ===")
        for xdf_id, ipa_symbol, url, reason in failed_details:
            print(f"  {xdf_id} -> {ipa_symbol}: {reason}")
    
    print(f"\n=== SUCCESS RATE ===")
    print(f"{success}/{len(XDF_AUDIO_MAPPING)} = {success/len(XDF_AUDIO_MAPPING)*100:.1f}%")


if __name__ == "__main__":
    main()
