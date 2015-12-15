#! /usr/bin/env python

import sys

wires = {}
dependencies = {}
backlog = {}

def set_dependency(a, b):
    """Set a to depend on b
    """
    d = dependencies.get(a)
    if d == None:
        d = set()
    d.add(b)
    dependencies[a] = d

def set_wire(a, operation, b, c):
    """Assign the value of operation on wire b to wire a
    """
    if operation == '->':
        res = b
    if operation == 'NOT':
        res = ~b
    elif operation == 'AND':
        res = b & c
    elif operation == 'OR':
        res = b | c
    elif operation == 'LSHIFT':
        res = b << c
    elif operation == 'RSHIFT':
        res = b >> c
    wires[a] = res & 0xFFFF #we need the & 0xFFFF part to make it 16 bit

def convert(wire):
    """If wire is actually a number, return it as an int. Otherwise return the
    signal that wire provides.
    """
    try:
        return int(wire)
    except ValueError:
        return wires.get(wire)

def execute_line(line):
    """Attempt to execute the instructions in the given line.
    """
    parts = line.split()
    c = None
    if len(parts) == 5:
        #AND, OR, LSHIFT, RSHIFT
        b, op, c, _, a = parts
        if convert(c) == None:
            set_dependency(a, c)
            return False
        c = convert(c)
    elif len(parts) == 4:
        #NOT
        op, b, _, a = parts
    elif len(parts) == 3:
        #signal provide ->
        b, op, a = parts
    if convert(b) == None:
        set_dependency(a, b)
        return False
    b = convert(b)
    set_wire(a, op, b, c)
    return True

def backtrack(wire, line):
    """Backtrack through dependencies until line gets executed
    """
    while not execute_line(line):
        w = list(dependencies[wire])[0]
        dependencies[wire].remove(w)
        prev_line = backlog.pop(w, None)
        if prev_line != None:
            backtrack(w, prev_line)

#process the input and work out dependencies
for line in sys.stdin:
    if not execute_line(line): #operation failed
        #put the line on the backlog
        wire = line.split()[-1]
        backlog[wire] = line

#go through the backlog, backtracking through dependencies
while len(backlog) > 0:
    wire, line = backlog.popitem()
    backtrack(wire, line)

#print out the result
for k, v in sorted(wires.iteritems()):
    print('%s: %d' % (k, v))
