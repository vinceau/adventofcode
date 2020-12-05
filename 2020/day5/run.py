import sys

def binary_space_partition(letter, lst):
    pivot = int(len(lst) / 2)
    if letter == "F" or letter == "L":
        return lst[:pivot]
    elif letter == "B" or letter == "R":
        return lst[pivot:]
    return lst


def partition(commands, max_length):
    lst = range(max_length)
    for letter in commands:
        lst = binary_space_partition(letter, lst)
    return lst[0]

def calculate_seat_id(row, column):
    return row * 8 + column

def find_seat(seats):
    """
    Our seat is the one which is missing a number.
    """
    seat_ids = seats.copy()
    seat_ids.sort()
    # Start tracking from the first number
    last_seat = seat_ids[0]
    for num in seat_ids[1:]:
        # Check if we missed a number
        if num == last_seat + 2:
            return last_seat + 1
        last_seat = num
    return -1

def main():
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
    max_id = max(seat_ids)
    print(f"largest seat id: {max_id}")


    print("part 2")
    my_seat = find_seat(seat_ids)
    print(f"my seat: {my_seat}")


if __name__ == "__main__":
    main()
