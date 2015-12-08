#! /usr/bin/env python

import sys

#part 1
def is_nice(word):
    if any(w in word for w in ['ab', 'cd', 'pq', 'xy']):
        return False
    vowel_count = sum(word.count(v) for v in ['a', 'e', 'i', 'o', 'u'])
    if vowel_count < 3:
        return False
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

nice = 0
for line in sys.stdin:
    if is_nice(line):
        nice += 1
print('Part 1: There are %d nice words' % nice)
