#! /usr/bin/env python

import sys

xpos = 0
ypos = 0
visited = set() #empty set

def gen_ident():
    return '%d,%d' % (xpos, ypos)

def visit(ch):
    global xpos, ypos
    if ch == '^':
        ypos += 1
    elif ch == '>':
        xpos += 1
    elif ch == 'v':
        ypos -= 1
    elif ch == '<':
        xpos -= 1
    visited.add(gen_ident())

#add starting house
visited.add(gen_ident())
for line in sys.stdin:
    for c in line:
        visit(c)
print('Total houses visited: %d' % len(visited))
