import sys

rows, cols = map(int, sys.stdin.readline().rstrip().split())

if rows == 1:
    print(1)
elif rows == 2:
    move = int((cols+1)//2)
    print(min(move, 4))
else:
    if cols < 7:
        print(min(4, cols))
    else:
        print(cols-2)