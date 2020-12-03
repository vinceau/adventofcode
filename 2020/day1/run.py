import sys

def find_pairs(nums):
  for i, num in enumerate(nums):
    for j, other_num in enumerate(nums):
      if i == j:
        continue
      if num + other_num == 2020:
        return num * other_num

def find_triples(nums):
  for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
      if i == j:
        continue
      for k, num3 in enumerate(nums):
        if k == i and k == j:
          continue
        if num1 + num2 + num3 == 2020:
          return num1 * num2 * num3

def main():
  nums = []
  for line in sys.stdin:
      num_string = line.strip()
      if num_string:
        nums.append(int(num_string))
  res = find_pairs(nums)
  print("part 1")
  print(res)

  res2 = find_triples(nums)
  print("part 2")
  print(res2)

if __name__ == "__main__":
    main()
