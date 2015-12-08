import sys
from operator import mul

def wrap(dims):
    l, w, h = map(int, dims.split('x'))
    nums = [l*w, w*h, h*l]
    return min(nums) + 2*sum(nums)

def ribbon(dims):
    nums = map(int, dims.split('x'))
    sides = list(nums)
    sides.remove(max(sides))
    return 2*sum(sides) + reduce(mul, nums, 1)

total = 0
ribbon_total = 0
for line in sys.stdin:
    total += wrap(line)
    ribbon_total += ribbon(line)
print('Total square feet required: %d' % total)
print('Total ribbon required: %d' % ribbon_total)
