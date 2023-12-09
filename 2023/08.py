import math


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/08_actual.txt')
    instructions, steps = parse_input(inp)

    total = count_nodes('AAA', instructions, steps)

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/08_actual.txt')
    instructions, steps = parse_input(inp)

    # Get nodes ending with A (starting nodes)
    nodes = []
    for node in steps.keys():
        if node[-1] == 'A':
            nodes.append(node)

    totals = []
    for node in nodes:
        totals.append(count_nodes(node, instructions, steps, ghost_mode=True))

    print('Part 2:', math.lcm(*totals))


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


def count_nodes(node: str, instructions: [], steps: {}, ghost_mode=False) -> int:
    """ Returns the number of nodes needed till the finish

    :param node: The starting node
    :param instructions: The instructions as a list
    :param steps: All the nodes with their steps
    :param ghost_mode: If the map is for a ghost
    :return: THe number of nodes to check till the finish.
    """
    total = 0

    while True:
        for instruction in instructions:
            node = steps[node][instruction]
            total += 1
            if not ghost_mode and node == 'ZZZ':
                return total
            elif ghost_mode and node[-1] == 'Z':
                return total


def get_input(file_path):
    with open(file_path) as f:
        return [s.strip() for s in f.readlines()]


if __name__ == '__main__':
    main()
