#!/usr/bin/python34
#
# q2_reducer.py:
# Reads key/value pairs from stdin, writes key/value pairs to stdout

import sys

def main(argv):
    try:
        oldWord   = None
        oldSum    = 0
        for line in sys.stdin:
            (key,value) = line.rstrip().split('\t')
            if key.startswith("fnard:-1 fnok:-1 cark:-1 gnuck:-1"):
                word = key
                if word!=oldWord:
                    if oldWord:
                        print("{}: {}".format(oldWord,oldSum))
                    oldWord = word
                    oldSum  = 0
                oldSum += int(value)
    except EOFError:
        pass
    if oldWord:
        print("{}: {}".format(oldWord,oldSum))
    return None

if __name__ == "__main__":
    main(sys.argv)

