import sys
from operator import mul

def wrap(dims):
    nums = map(int, dims.split('x'))
    l = nums[0]
    w = nums[1]
    h = nums[2]
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
