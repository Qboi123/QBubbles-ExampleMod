from qbubbles.__main__ import Main

import sys
import os


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath("examplemod"))
    sys.argv.append("gameDir=.")
    from python import __main__
    main = Main()
    main.mainloop()
