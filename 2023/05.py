def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/05_actual.txt')

    input_parsed = parse_input(inp)

    steps = {
        0: 'seed-to-soil',
        1: 'soil-to-fertilizer',
        2: 'fertilizer-to-water',
        3: 'water-to-light',
        4: 'light-to-temperature',
        5: 'temperature-to-humidity',
        6: 'humidity-to-location',
    }


    min_value = None
    for seed in input_parsed['seeds']:
        value = int(seed)
        for step in steps.values():
            #print(f'{value}->', end='')
            value = get_value(old_value=value, step=step, inp=input_parsed)
            #print(value)
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value

    print('Part 1:', min_value)


def part_2():
    # TODO
    ...


def get_value(old_value, step, inp):
    inp = inp[step]
    for numbers in inp:
        destination_start = numbers[0]
        source_start = numbers[1]
        range_length = numbers[2]

        if source_start <= old_value <= source_start+range_length:
            return destination_start + (old_value - source_start)

    return old_value


def parse_input(inp):
    input_parsed = {}

    current_line = ''
    titles = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    for index, line in enumerate(inp):
        line = line.strip()

        if not line:
            continue

        if index == 0:
            line = line.lstrip('seeds:')
            input_parsed['seeds'] = line.lstrip('seeds:').split()
            continue

        if line.rstrip(' map:') in titles:
            current_line = line.rstrip(' map:')
            input_parsed[current_line] = []
            continue

        destination_range_start, source_range_start, range_length = line.split()
        input_parsed[current_line].append([int(destination_range_start), int(source_range_start), int(range_length)])

    return input_parsed


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == '__main__':
    main()
