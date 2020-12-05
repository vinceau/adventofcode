import re
import sys

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

def binary_space_partition(front_or_back, lst):
    pivot = int(len(lst) / 2)
    if front_or_back == "front":
        return lst[:pivot]
    elif front_or_back == "back":
        return lst[pivot:]
    return lst


def partition(commands, max_length):
    lst = range(max_length)
    for letter in commands:
        if letter == "F" or letter == "L":
            lst = binary_space_partition("front", lst)
        elif letter == "B" or letter == "R":
            lst = binary_space_partition("back", lst)
    return lst[0]

def calculate_seat_id(row, column):
    return row * 8 + column

def find_seat(seats):
    seat_ids = seats.copy()
    seat_ids.sort()
    last_seat = seat_ids[0]
    for num in seat_ids[1:]:
        if num == last_seat + 2:
            return last_seat + 1
        last_seat = num
    return -1

def main():
    # allow the map to be indexable
    seat_ids = []
    for line in sys.stdin:
        l = line.strip()
        if l:
            row_command = l[:-3]
            col_command = l[-3:]
            row = partition(row_command, 128)
            col = partition(col_command, 8)
            seat_ids.append(calculate_seat_id(row, col))

    print("part 1")
    max_id = f"largest seat id: {max(seat_ids)}"
    print(max_id)


    print("part 2")
    my_seat = find_seat(seat_ids)
    print(f"my seat: {my_seat}")


if __name__ == "__main__":
    main()
