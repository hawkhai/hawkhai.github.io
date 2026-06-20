#encoding=utf8
import os, sys
from mdrstrip.runtime import *
from mdrstrip.config import *
from mdrstrip.resources import *
from mdrstrip.references import *
from mdrstrip.filesystem import *
from mdrstrip.formatter import *
from mdrstrip.runner import main, mainw, mainfilew

__file__ = os.path.abspath(__file__)

if __name__ == "__main__":
    print(sys.argv)
    import cProfile
    if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
        workdir = sys.argv[1]
        @CWD_DIR_RUN(workdir)
        def maingo():
            cProfile.run("mainw()") if DEBUG else mainw()
        maingo()
    else:
        cProfile.run("mainw()") if DEBUG else mainw()
        os.system(r"cd invisible & {} tempd.py encrypt".format(getPythonExe(),))
    close_cache()
    print(parsePythonCmdx(SCRIPT_FILE))
