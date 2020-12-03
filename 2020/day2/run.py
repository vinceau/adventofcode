import sys

def is_valid(letter, min, max, password):
    counts = password.count(letter)
    return counts >= min and counts <= max

def is_valid_pos(letter, pos1, pos2, password):
    valid = 0
    if password[pos1-1] == letter:
        valid += 1
    if password[pos2-1] == letter:
        valid += 1
    return valid == 1

def main():
  valid = 0
  valid_part2 = 0
  for line in sys.stdin:
      l = line.strip()
      if l:
          [rule_text, password] = l.split(": ")
          [rule_min, letter] = rule_text.split(" ")
          [min_text, max_text] = rule_min.split("-")
          if is_valid(letter, int(min_text), int(max_text), password):
              valid += 1
          if is_valid_pos(letter, int(min_text), int(max_text), password):
              valid_part2 += 1

  print("part 1")
  print(valid)

  print("part 2")
  print(valid_part2)

if __name__ == "__main__":
    main()
