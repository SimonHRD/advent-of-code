import logging
logging.basicConfig(level=logging.INFO)


def main():
    part_1()
    part_2()


def part_1():
    patterns = get_input('./inputs/13_actual.txt')

    total = 0
    for pattern in patterns:
        value = get_reflection_value(pattern)
        total += value

    print('Part 1:', total)


def part_2():
    patterns = get_input('./inputs/13_actual.txt')

    total = 0
    for pattern in patterns:
        value = get_reflection_value(pattern, smudge=True)
        total += value

    print('Part 2:', total)


def get_reflection_value(pattern: [[str]], smudge: bool = False) -> int:
    """ Returns the reflection value of a given pattern

    :param pattern: The pattern as a [[str]]
    :param smudge: If smudge mode is activated
    :return: The reflection value
    """
    # Check horizontally
    last_line = ''
    for index, line in enumerate(pattern):
        differences = 0
        if smudge:
            for i in range(len(last_line)):
                if not line[i] == last_line[i]:
                    differences += 1
        if (line == last_line) or (smudge and differences == 1):
            rows_above, rows_below = index, len(pattern) - index
            rows_to_check = min(rows_above, rows_below)
            if is_mirroring_horizontally(index, rows_to_check, pattern, smudge):
                return index * 100

        last_line = line

    # Check vertically
    last_line = ''
    current_line = ''
    for i in range(len(pattern[0])):
        differences = 0

        for j in range(len(pattern)):
            current_line += pattern[j][i]

        if smudge:
            for k in range(len(last_line)):
                if not current_line[k] == last_line[k]:
                    differences += 1

        if (current_line == last_line) or (smudge and differences == 1):
            rows_left = i
            rows_right = len(pattern[0]) - i
            rows_to_check = min(rows_left, rows_right)
            if is_mirroring_vertically(i, rows_to_check, pattern, smudge):
                return i

        last_line = current_line
        current_line = ''

    logging.error(f'No reflection found for pattern:\n{pattern}')
    return 0


def get_patterns(inp: []) -> [[str]]:
    pattern = []
    patterns = []
    for line in inp:
        if not line:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)
    return patterns


def is_mirroring_horizontally(index, rows_to_check, pattern, smudge: bool):
    """ Checks if a line reelects on a given index horizontally

    :param index: The index where it potentially mirrors
    :param rows_to_check: Number of rows it mirrors
    :param pattern: The pattern
    :param smudge: If smudge mode is activated
    :return:
    """
    differences = 0
    for i in range(0, rows_to_check):
        if (not smudge and not pattern[index - i - 1] == pattern[index + i]) or (smudge and differences > 1):
            return False
        elif smudge and not pattern[index - i - 1] == pattern[index + i]:
            for k in range(len(pattern[index - i - 1])):
                if not pattern[index - i - 1][k] == pattern[index + i][k]:
                    differences += 1
    if (smudge and differences == 0) or (smudge and differences >= 2):
        return False
    return True


def is_mirroring_vertically(index, rows_to_check, pattern, smudge: bool):
    """ Checks if a line reelects on a given index vertically

    :param index: The index where it potentially mirrors
    :param rows_to_check: Number of rows it mirrors
    :param pattern: The pattern
    :param smudge: If smudge mode is activated
    :return:
    """
    differences = 0
    for i in range(rows_to_check):
        line_left = ''
        line_right = ''
        for j in range(len(pattern)):
            line_left += pattern[j][index - i - 1]
            line_right += pattern[j][index + i]
        if (not smudge and not line_left == line_right) or (smudge and differences > 1):
            return False
        if smudge and not line_left == line_right:
            for k in range(len(line_left)):
                if not line_left[k] == line_right[k]:
                    differences += 1
    if smudge and differences == 0:
        return False
    return True


def get_input(file_path):
    with open(file_path) as f:
        lines = [s.strip() for s in f.readlines()]
    return get_patterns(lines)


if __name__ == '__main__':
    main()
