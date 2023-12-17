from pprint import pprint


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/17_actual.txt')

    total = 0

    for part in inp:
        total += get_value(part)

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/17_test.txt')

    total = 0

    print('Part 2:', total)


def get_value(part):
    value = 0
    for c in part:
        ascii_value = ord(c)
        value += ascii_value
        value *= 17
        value = value % 256
    return value



def get_input(file_path):
    with open(file_path) as f:
        inp = [s.strip() for s in f.readlines()]
        return inp[0].split(',')


if __name__ == '__main__':
    main()
