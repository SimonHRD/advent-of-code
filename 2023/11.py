from pprint import pprint


def main():
    part_1()
    part_2()


def part_1():
    universe = get_input('./inputs/11_actual.txt')

    universe = expand_universe(universe)

    total = 0
    for galaxy, coordinates in universe.items():
        for i in range(galaxy+1, len(universe)+1):
            total += abs(coordinates[0] - universe[i][0]) + abs(coordinates[1] - universe[i][1])

    print('Part 1:', total)


def part_2():
    universe = get_input('./inputs/11_actual.txt')

    universe = expand_universe(universe, expand_high=True)

    total = 0
    for galaxy, coordinates in universe.items():
        for i in range(galaxy + 1, len(universe) + 1):
            total += abs(coordinates[0] - universe[i][0]) + abs(coordinates[1] - universe[i][1])

    print('Part 2:', total)


def expand_universe(universe, expand_high=False):
    # horizontally
    indexes_horizontally = []
    for index, row in enumerate(universe):
        if row.count('#') == 0:
            indexes_horizontally.append(index)

    # vertically
    indexes_vertically = []
    for i in range(len(universe[0])):
        empty_row = True
        for row in universe:
            if row[i] == '#':
                empty_row = False
                break
        if empty_row:
            indexes_vertically.append(i)

    cnt = 1
    galaxies = {}
    for i, row in enumerate(universe):
        if expand_high:
            horizontally = (sum(c < i for c in indexes_horizontally) * 1000000) - \
                           sum(c < i for c in indexes_horizontally)
        else:
            horizontally = (sum(c < i for c in indexes_horizontally))
        for j, c in enumerate(row):
            if expand_high:
                vertically = (sum(c < j for c in indexes_vertically) * 1000000) - \
                             sum(c < j for c in indexes_vertically)
            else:
                vertically = (sum(c < j for c in indexes_vertically))
            if c == '#':
                galaxies[cnt] = (i+horizontally, j+vertically)
                cnt += 1
    return galaxies


def get_input(file_path):
    with open(file_path) as f:
        return [s.strip() for s in f.readlines()]


if __name__ == '__main__':
    main()
