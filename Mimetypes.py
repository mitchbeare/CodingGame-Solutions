import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.


mimedict = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()

    mimedict[ext.lower()] = mt
    
print(mimedict, file=sys.stderr)

for i in range(q):
    fname = input()  # One file name per line.
    print(fname, file=sys.stderr)
    ext = ''
    try:
        ext = re.split("(\.\w+$)",fname)[1]
        ext = ext.replace('.', '')
    except:
        ext = 'none found'
    try:
        mime = mimedict[ext.lower()]

        print(mime)
    except:
        print ('UNKNOWN')



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
