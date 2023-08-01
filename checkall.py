import os, sys
print(sys.argv)

for line in r"""
python3 reindent.py -r .
python3 headfmt.py
python3 mdimage.py format
python3 mdurl.py format
python3 mdimage.py format
python3 mdrstrip.py format copyres {} {}
""".format(
    "ignoreerr" if "ignoreerr" in sys.argv else "",
    "rebuild" if "rebuild" in sys.argv else ""
).split("\n"):
    line = line.strip()
    if not line: continue
    if "quick" in sys.argv and line.find("headfmt.py") != -1:
        continue
    os.system(line)

exit(0)
