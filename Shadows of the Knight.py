import sys
import math

"""
Your mission is to program the device so that it indicates the location
of the next window Batman should jump to in order to reach the bombs' room as soon as possible.

Buildings are represented as a rectangular array of windows,
the window in the top left corner of the building is at index (0,0).

 Write an action using print
 To debug: print("Debug messages...", file=sys.stderr)
    
 Auto-generated code below aims at helping you parse
 the standard input according to the problem statement.
"""
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
# maximum number of turns before game over.
n = int(input())
# x0: initial x co-ord
# y0: initial y co-ord
x0, y0 = [int(i) for i in input().split()]
# =============== End provided inputs =====================

minX = 0;
minY = 0;
maxX = w - 1;
maxY = h -1;

# 2d binary search:

# game loop

print(w, file=sys.stderr)
print(h, file=sys.stderr)
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Test for movement direction
    if len(bomb_dir) > 1:
        # X direction
        if 'L' in bomb_dir:
            maxX = x0 - 1
        elif 'R' in bomb_dir:
            minX = x0 + 1
        # Y direction
        if 'U' in bomb_dir:
            maxY = y0 - 1
        else:
            minY = y0 + 1
    else:
        if 'L' in bomb_dir:
            maxX = x0 - 1
        elif 'R' in bomb_dir:
            minX = x0 + 1
        elif 'U' in bomb_dir:
            maxY = y0 - 1
        else:
            minY = y0 + 1
    
    # Calculate where to move to
    x0 = (maxX + minX) // 2
    y0 = (maxY + minY) // 2

    # the location of the next window Batman should jump to.
    print("{0} {1}".format(x0, y0))
