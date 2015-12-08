#! /usr/bin/env python

import sys
import md5

def find(key, start):
    answer = 1
    m = md5.new()
    m.update(key + str(answer))
    while m.hexdigest()[:len(start)] != start:
        answer += 1
        m = md5.new()
        m.update(key + str(answer))
    return answer

for line in sys.stdin:
    key = line.strip()
    print('Part 1: Answer to %s is %d' % (key, find(key, '00000')))
    print('Part 2: Answer to %s is %d' % (key, find(key, '000000')))
