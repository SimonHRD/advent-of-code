from collections import Counter


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/09_actual.txt')

    total = 0

    for numbers in inp:
        numbers = [int(n) for n in numbers]
        total += get_value_for_numbers(numbers)

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/09_actual.txt')

    total = 0

    for numbers in inp:
        numbers = [int(n) for n in numbers]
        total += get_value_for_numbers(numbers[::-1])

    print('Part 2:', total)


def get_value_for_numbers(nums: []) -> int:
    """ Calculates the next number in the given number row

    :param nums: list of numbers
    :return: THe next number in the number row
    """
    numbers: [[int]] = [nums]

    while True:
        nums = []
        for index in range(1, len(numbers[-1])):
            nums.append(numbers[-1][index] - numbers[-1][index-1])
        numbers.append(nums)

        counter = Counter(numbers[-1])
        most_common = counter.most_common(1)[0][0]
        if most_common == 0 and len(counter) == 1:
            return sum(x[-1] for x in numbers)


def get_input(file_path):
    with open(file_path) as f:
        return [s.strip().split(' ') for s in f.readlines()]


if __name__ == '__main__':
    main()
