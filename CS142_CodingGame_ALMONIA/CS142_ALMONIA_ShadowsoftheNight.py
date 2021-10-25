import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
a, b, c, d = 0, h-1, 0, w-1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir[0] == 'D' :
        a = y+1
    if bomb_dir[0] == 'U' :
        b = y-1
    if bomb_dir[-1] == 'R' :
        c = x+1
    if bomb_dir[-1] == 'L' :
        d = x-1
    x = int((c+d)/2)
    y = int((a+b)/2)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print (str(x)+' '+str(y))  
    # the location of the next window Batman should jump to.