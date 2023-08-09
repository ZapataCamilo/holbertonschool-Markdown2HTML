#!/usr/bin/python3
'''A script markdown2html.py that takes an argument of 2 strings: -
First argument is the name of the Markdown file -
Second argument is the output file name, makes no change'''
import sys

def mark(*args):
    # Take 2 arguments
    f = len(sys.argv)

    if f <= 2:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)
    try:
        file = open(sys.argv[1])
        file.close()
    except:
        print('Missing', sys.argv[1], file=sys.stderr)
        exit(1)
    if __name__ == '__main__':
        mark(sys.argv)