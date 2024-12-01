def main():
    part_1()
    part_2()


def part_1():
    left, right = get_input('./inputs/01_actual.txt')
    left.sort()
    right.sort()

    count = sum(abs(left_num - right_num) for left_num, right_num in zip(left, right))

    print('Part 1: ', count)


def part_2():
    left, right = get_input('./inputs/01_actual.txt')
    count = sum(num * right.count(num) for num in left)
    print('Part 2: ', count)


def get_input(file_path: str) -> ([], []):
    left = []
    right = []

    with open(file_path) as f:
        for line in f.readlines():
            x, y = (int(i) for i in line.split())
            left.append(x)
            right.append(y)
    return left, right


if __name__ == '__main__':
    main()
