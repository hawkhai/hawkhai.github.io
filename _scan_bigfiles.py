#encoding=utf8
"""
读取 config/mdrstrip_bigfiles.txt，对每条记录的文件重新计算 md5，
输出需要更新的行（旧md5 -> 新md5）。
"""
import sys, os, re
sys.path.append('..')
from pythonx.funclib import getFileSrcMd5z

BIGFILE = 'config/mdrstrip_bigfiles.txt'

with open(BIGFILE, encoding='utf8') as f:
    lines = f.readlines()

new_lines = []
changed = 0
for line in lines:
    stripped = line.rstrip('\n')
    # 注释或空行，原样保留
    if not stripped.strip() or stripped.strip().startswith('#'):
        new_lines.append(line)
        continue

    # 格式: <md5> # <filepath> # <size>
    m = re.match(r'^([0-9a-f]{32})\s+#\s+(.+?)\s+#', stripped, re.IGNORECASE)
    if not m:
        new_lines.append(line)
        continue

    old_md5 = m.group(1)
    fpath    = m.group(2).strip()

    # 规范化路径（去掉前缀 .\ 或 ./）
    fpath_norm = fpath.lstrip('.').lstrip('/').lstrip('\\')
    fpath_norm = fpath_norm.replace('\\', os.sep).replace('/', os.sep)

    if not os.path.exists(fpath_norm):
        print('NOT FOUND:', fpath_norm)
        new_lines.append(line)
        continue

    size   = os.path.getsize(fpath_norm)
    new_md5 = getFileSrcMd5z(fpath_norm, assertx=False)

    if new_md5 and new_md5 != old_md5:
        size_str = '%.1f MB' % (size / 1024 / 1000)
        new_line = stripped.replace(old_md5, new_md5)
        # 更新 size 注释
        new_line = re.sub(r'#\s+[\d.]+ MB\s*$', '# ' + size_str, new_line)
        print('UPDATED:', old_md5, '->', new_md5, '|', fpath_norm)
        new_lines.append(new_line + '\n')
        changed += 1
    else:
        new_lines.append(line)

if changed:
    with open(BIGFILE, 'w', encoding='utf8') as f:
        f.writelines(new_lines)
    print('Written', changed, 'updates to', BIGFILE)
else:
    print('All md5s up to date, no changes needed.')
