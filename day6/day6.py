#! /usr/bin/env python

import sys

size = 1000

#part 1
matrix = [[False] * size for _ in range(size)]

def count(mat):
    return sum(sum(x) for x in mat)

def turn(onoff, coord1, coord2):
    x1, y1 = [int(x) for x in coord1.split(',')]
    x2, y2 = [int(x) for x in coord2.split(',')]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            matrix[x][y] = onoff

def toggle(coord1, coord2):
    x1, y1 = [int(x) for x in coord1.split(',')]
    x2, y2 = [int(x) for x in coord2.split(',')]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            matrix[x][y] = not matrix[x][y]

#part 2
matrix2 = [[0] * size for _ in range(size)]

def turn2(onoff, coord1, coord2):
    x1, y1 = [int(x) for x in coord1.split(',')]
    x2, y2 = [int(x) for x in coord2.split(',')]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if onoff:
                matrix2[x][y] += 1
            else:
                matrix2[x][y] -= 1
                if matrix2[x][y] < 0:
                    matrix2[x][y] = 0

def toggle2(coord1, coord2):
    x1, y1 = [int(x) for x in coord1.split(',')]
    x2, y2 = [int(x) for x in coord2.split(',')]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            matrix2[x][y] += 2

for line in sys.stdin:
    if len(line.split()) == 5:
        _, onoff, c1, _, c2 = line.split()
        turn(onoff == 'on', c1, c2)
        turn2(onoff == 'on', c1, c2)
    else:
        _, c1, _, c2 = line.split()
        toggle(c1, c2)
        toggle2(c1, c2)

print('Part 1: There are %d lights that are on' % count(matrix))
print('Part 2: The total brightness is %d' % count(matrix2))
