import os, sys
import time

def main():
    print(sys.argv)

    atime = time.time()
    litime = []

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

        xtime = time.time()
        code = os.system(line)
        ytime = time.time()
        litime.append([code, line, ytime - xtime])

    btime = time.time()
    print()
    print("***" * 30)
    for code, line, itime in litime:
        print(code, "%-8.2f"%itime, line)
    print("***" * 30)
    print("%-8.2f"%(btime - atime))
    #exit(0)

if __name__ == "__main__":
    main()
    print("ok")
