def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/08_actual.txt')
    instructions, steps = parse_input(inp)

    total = 0

    current_key = 'AAA'
    while not current_key == 'ZZZ':
        for instruction in instructions:
            current_key = steps[current_key][instruction]
            total += 1
            if current_key == 'ZZZ':
                break

    print('Part 1:', total)


def part_2():
    # TODO: Part 2
    ...


def parse_input(inp):
    instructions = inp[0]
    steps = inp[2:]

    steps_parsed = {}
    for step in steps:
        k, v = step.split(' = ')
        steps_parsed[k] = {
            'L': v[1:-1].split(', ')[0],
            'R': v[1: -1].split(', ')[1],
        }

    return list(instructions), steps_parsed


def get_input(file_path):
    with open(file_path) as f:
        return [s.strip() for s in f.readlines()]


if __name__ == '__main__':
    main()
