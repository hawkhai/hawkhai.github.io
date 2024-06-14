import os, sys
import time

g_colorPrint = False
# termcolor 貌似存在 bug，colorama 可以用。
def colorPrint(*args, color="red"):
    import colorama
    global g_colorPrint
    if not g_colorPrint:
        g_colorPrint = True
        colorama.init(autoreset=True)

    config = {
        "red": colorama.Fore.RED,
        "green": colorama.Fore.GREEN,
        "yellow": colorama.Fore.YELLOW,
        "blue": colorama.Fore.BLUE,
        "magenta": colorama.Fore.MAGENTA,
        "cyan": colorama.Fore.CYAN,
        "white": colorama.Fore.WHITE,
    }
    msg = " ".join([str(arg) for arg in args])
    print(config[color] + msg + colorama.Style.RESET_ALL)

# https://www.jonathan-petitcolas.com/ascii-art-converter/
def printfail(msg):
    assert len(msg) == 8, msg
    colorPrint(r"""
                 !mB$@Mj.                           ')j'
               .w@Y`  _%B!                 U@%|     x@&^
              .q$w     I].                          Y$o'
              IBB<                                  C$Z
              1$o.              :w%&b@%~    )$o     Z$J
             ,Y$@&8%B@@@C     +%@f.  /$[    ?$*     q$c
         .{u-:?@#'          "&@n    +B$k.   >@o     d@r
              !@&,        'q@0.   'CBz%*"   ;@*     b@f
              :%@~       ,oB|   .{%o;:%W!   ,%W    .b@)
              "W@(      'o@j  `|8a?  ;%%-   `W@;   .k$z
              `#@u      'q$%W@MX,    "&@J   .h$n    1@%<
              'o@Y         .                 "!"
{%s}       J@x
    """.replace("{%s}", msg))

def printok(msg):
    assert len(msg) == 8, msg
    colorPrint(r"""
                          t%&.
                          C$@'
                          c$@^
                          n$@,
             ~M@h;''      f$@l    .+YW@B$*`
            XBB?>h@%x     {@@~ .}h@w-^
           (@W:   `)W@0'  ~@@zZ@Q>
          :B$(      ,@@v  <$$W-
          ?@@!      |$%"  !#@@%b?
          i@$f.  '|%@X.    u@W..r8@@or^'.
{%s}    C*MMMoC"       ]@@+     .{QOx
    """.replace("{%s}", msg), color="white")

def main():
    print(sys.argv)

    atime = time.time()
    litime = []

    for line in r"""
python3 reindent.py --newline -r .
python3 reindent.py --newline -r invisible
python3 headfmt.py
python3 mdimage.py format
python3 mdurl.py format
python3 mdimage.py format
python3 mdrstrip.py format copyres {} {} {}
""".format(
        "ignoreerr" if "ignoreerr" in sys.argv else "",
        "rebuild" if "rebuild" in sys.argv else "",
        "netfake" if ("netfake" in sys.argv or "fakenet" in sys.argv) else "",
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
    codek = 0
    print()
    print("***" * 30)
    for code, line, itime in litime:
        print(code, "%-8.2f"%itime, line)
        codek += code
    print("***" * 30)
    msg = "%-8.2f"%(btime - atime)
    if codek == 0:
        printok(msg)
    else:
        printfail(msg)
    #exit(0)

if __name__ == "__main__":
    main()
    print("ok")
