#! /usr/bin/env python

import sys

xpos = 0
ypos = 0
visited = set()

santax = 0
santay = 0
robox = 0
roboy = 0
new_visited = set()

santas_turn = True

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

def santa_visit(ch):
    global santax, santay, santas_turn
    if ch == '^':
        santay += 1
    elif ch == '>':
        santax += 1
    elif ch == 'v':
        santay -= 1
    elif ch == '<':
        santax -= 1
    new_visited.add('%d,%d' % (santax, santay))
    santas_turn = False

def robo_visit(ch):
    global robox, roboy, santas_turn
    if ch == '^':
        roboy += 1
    elif ch == '>':
        robox += 1
    elif ch == 'v':
        roboy -= 1
    elif ch == '<':
        robox -= 1
    new_visited.add('%d,%d' % (robox, roboy))
    santas_turn = True

#add starting house
visited.add(gen_ident())
new_visited.add(gen_ident())

for line in sys.stdin:
    for c in line:
        #part one
        visit(c)
        #part two
        if santas_turn:
            santa_visit(c)
        else:
            robo_visit(c)
print('Part 1: Total houses visited: %d' % len(visited))
print('Part 2: Total houses visited: %d' % len(new_visited))
