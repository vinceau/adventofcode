import sys

level = 0
char_count = 1
find_level = -1 #which character takes us to this level?
found_char = None
for line in sys.stdin:
    for c in line:
        if c == '(':
            level += 1
        else:
            level -= 1
        if level == find_level:
            found_char = char_count
        if not found_char:
            char_count += 1
print('Final floor %d' % level)
if found_char:
    print('Reached floor %d after at character %d' % (find_level, found_char))
else:
    print('Santa never reaches floor %d' % find_level)
