def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/02_actual.txt')

    total = 0

    for line in inp:
        line = line.strip()
        game_id, cubes = line.split(': ')
        possible = check_possibility(cubes)

        if possible:
            game_id = int(game_id.lstrip('Game '))
            total += game_id

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/02_actual.txt')

    total = 0

    for line in inp:
        line = line.strip()
        game_id, cubes = line.split(': ')

        red = 0
        blue = 0
        green = 0

        sets = cubes.split(';')
        for s in sets:
            pairs = s.strip().split(', ')
            for pair in pairs:
                amount, color = pair.split(' ')
                if color == 'red' and int(amount) > red:
                    red = int(amount)
                elif color == 'green' and int(amount) > green:
                    green = int(amount)
                elif color == 'blue' and int(amount) > blue:
                    blue = int(amount)
        total += (red * green * blue)

    print('Part 2:', total)


def check_possibility(cubes: []) -> bool:
    """ A game is only playable when there are no more than 12 red, 13 green and 14 blue cube for each set

    :param cubes: List with all sets of a game
    :return: True if the game is playable
    """
    sets = cubes.split(';')
    for s in sets:
        pairs = s.strip().split(', ')
        for pair in pairs:
            amount, color = pair.split(' ')
            if (color == 'red' and int(amount) > 12 or
                    color == 'green' and int(amount) > 13 or
                    color == 'blue' and int(amount) > 14):
                return False
    return True


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == '__main__':
    main()
