#! /usr/bin/env python

import sys

wires = {}
dependencies = {}
backlog = {}

def valid_dependency(w):
    if w in wires.keys():
        return False
    return type(w).__name__ == 'str' and not w.isdigit()

def set_dependency(a, b):
    d = dependencies.get(a)
    if d == None:
        d = set()
    if valid_dependency(b):
        d.add(b)
    dependencies[a] = d

def set_wire(a, operation, b, c):
    """Assign the value of operation on wire b to wire a
    """
    try:
        b = int(b)
    except ValueError:
        try:
            b = wires[b]
        except KeyError:
            set_dependency(a, b)
            return False
    if c:
        try:
            c = int(c)
        except ValueError:
            try:
                c = wires[c]
            except KeyError:
                set_dependency(a, c)
                return False
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
    return True

def execute_line(line):
    parts = line.split()
    c = None
    if len(parts) == 5:
        #AND, OR, LSHIFT, RSHIFT
        b, op, c, _, a = parts
    elif len(parts) == 4:
        #NOT
        op, b, _, a = parts
    elif len(parts) == 3:
        #signal provide ->
        b, op, a = parts
    return set_wire(a, op, b, c)

def backtrack(wire, line):
    while not execute_line(line):
        w = list(dependencies[wire])[0]
        dependencies[wire].remove(w)
        prev_line = backlog.get(w)
        if prev_line == None:
            continue
        if not execute_line(prev_line):
            #sigh, it depends on something else
            backtrack(w, prev_line)
            execute_line(prev_line)

for line in sys.stdin:
#   print(line.strip())
    if not execute_line(line): #operation failed
        wire = line.split()[-1]
        backlog[wire] = line

while len(backlog) > 0:
    wire, line = backlog.popitem()
    backtrack(wire, line)

for k, v in sorted(wires.iteritems()):
    print('%s: %d' % (k, v))
