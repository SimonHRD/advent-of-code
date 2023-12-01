NUMS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/01_actual.txt')

    total = 0

    for line in inp:
        first = get_first_num(line)
        last = get_last_num(line)

        number = first * 10 + last
        total += number
    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/01_actual.txt')

    total = 0

    for line in inp:
        first = get_first_num(line, with_words=True)
        last = get_last_num(line, with_words=True)

        number = first * 10 + last
        total += number
    print('Part 2:', total)


def get_first_num(line: str, with_words: bool = False) -> int:
    """ Returns the first number in a string.

    :param line: The string
    :param with_words: Optional parameter to check number written as words
    :return: THe number as integer
    """
    for i, c in enumerate(line):
        if c.isdigit():
            return int(c)
        if with_words:
            for n in NUMS.keys():
                par = line[i:len(n) + i]
                if par in NUMS:
                    return int(NUMS[par])


def get_last_num(line: str, with_words: bool = False) -> int:
    """ Returns the last number in a string.

    :param line: The string
    :param with_words: Optional parameter to check number written as words
    :return: THe number as integer
    """
    reversed_line = line[::-1].strip()
    for i, c in enumerate(reversed_line):
        if c.isdigit():
            return int(c)
        if with_words:
            for n in NUMS.keys():
                par = reversed_line[i:len(n) + i][::-1]
                if par in NUMS:
                    return int(NUMS[par])


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == '__main__':
    main()
