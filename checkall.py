import os, sys

for line in r"""
python3 reindent.py -r .
python3 headfmt.py
python3 mdimage.py format
python3 mdurl.py format
python3 mdimage.py format
python3 mdrstrip.py format copyres ignoreerr
""".split("\n"):
    line = line.strip()
    if not line: continue
    os.system(line)

exit(0)
