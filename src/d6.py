#! /usr/bin/env python

import sys

size = 1000

matrix = [[False for _ in range(size)] for _ in range(size)]

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

def count():
    c = 0
    for x in range(size):
        for y in range(size):
            if matrix[x][y]:
                c += 1
    return c

for line in sys.stdin:
    if len(line.split()) == 5:
        _, onoff, c1, _, c2 = line.split()
        turn(onoff == 'on', c1, c2)
    else:
        _, c1, _, c2 = line.split()
        toggle(c1, c2)

print('Part 1: There are %d lights that are on' % count())
