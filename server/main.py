#!/usr/bin/env python3

from comm import Comm
from game import Game
import sys


def main(argv):
    c = Comm()
    g = Game()
    while(True):
        c.wait()
        print(c.receive())
        # TODO: g.begin()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))