import sys

def count_trees(slope, lines):
    movement_x = slope[0]
    movement_y = slope[1]

    current_x = 0
    current_y = 0

    y_to_go = len(lines) - 1
    x_length = len(lines[0])

    tree_count = 0

    while current_y < y_to_go:
        current_y += movement_y
        current_x = (current_x + movement_x) % x_length

        is_tree = lines[current_y][current_x] == '#'
        if is_tree:
            tree_count += 1

    return tree_count

def main():
    # allow the map to be indexable
    lines = []
    for line in sys.stdin:
        l = line.strip()
        if l:
            lines.append(l)

    print("part 1")
    print(count_trees((3,1), lines))

    answer = 1
    slopes = [(1, 1), (3,1), (5,1), (7,1), (1,2)]
    for slope in slopes:
        answer *= count_trees(slope, lines)

    print("part 2")
    print(answer)

if __name__ == "__main__":
    main()
