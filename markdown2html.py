#!/usr/bin/python3
'''A script markdown2html.py that takes an argument of 2 strings: -
First argument is the name of the Markdown file -
Second argument is the output file name, makes no change'''
import sys
import markdown

def mark(*args):
    # Take 2 strings arguments 
    f = len(sys.argv)

    if f < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit (1)
    try:
        file = open(sys.argv[1], 'r')
        txt = file.read()
        copy = markdown.markdown(txt)
        file.close()
        with open(sys.argv[2], 'w') as f:
            f.write(copy)
    except:
        print("Missing", sys.argv[1], file=sys.stderr)
        exit(1)
if __name__ == '__main__':
    mark(sys.argv)