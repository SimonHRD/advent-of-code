from pprint import pprint


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/03_actual.txt')

    input_parsed = parse_input(inp)

    total = 0
    valid_nums_indexes = {}

    # Check for each line the valid numbers
    for key, values in input_parsed.items():
        # Check each number in a line if it is valid
        for number in values['numbers']:
            is_valid = False
            min_index, max_index = min(number), max(number)

            # Check num - same line
            if min_index - 1 in values['symbols'] or max_index + 1 in values['symbols']:
                is_valid = True

            # Check num - previous line
            if key > 0:
                for i in range(min_index - 1, max_index + 2):
                    if i in input_parsed[key - 1]['symbols']:
                        is_valid = True

            # Check num - next line
            if key < len(input_parsed) - 1:
                for i in range(min_index - 1, max_index + 2):
                    if i in input_parsed[key + 1]['symbols']:
                        is_valid = True

            # If number is valid add the indexes to the valid_nums_indexes dict
            if is_valid:
                if key not in valid_nums_indexes:
                    valid_nums_indexes[key] = []
                valid_nums_indexes[key].append(number)

    # Get the numbers from the valid_nums_indexes and add them to the total
    for key, indexes in valid_nums_indexes.items():
        for index in indexes:
            number_extracted = []
            for number in index:
                number_extracted.append(inp[key][number])
            total += int(''.join(number_extracted))

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/03_actual.txt')
    input_parsed = parse_input_part2(inp)

    total = 0

    # Check for each line the symbol
    for key, values in input_parsed.items():
        if values['symbols']:
            # Check each symbol (star) in a line if it is valid
            for star in values['symbols']:
                numbers = []

                # Check same line
                for number in values['numbers']:
                    if star - 1 in number or star + 1 in number:
                        numbers.append({key: number})

                # Check previous line
                if key > 0:
                    for i in range(star - 1, star + 2):
                        for number in input_parsed[key - 1]['numbers']:
                            if i in number:
                                numbers.append({key - 1: number})

                # Check next line
                if key < len(input_parsed) - 1:
                    for i in range(star - 1, star + 2):
                        for number in input_parsed[key + 1]['numbers']:
                            if i in number:
                                numbers.append({key + 1: number})

                # Removes duplicated numbers
                numbers = remove_duplicates(numbers)

                # If the symbol has two numbers then add the product to the total
                if len(numbers) == 2:
                    nums = []
                    for number in numbers:
                        for k, v in number.items():
                            number_extracted = []
                            for n in v:
                                number_extracted.append(inp[k][n])
                            nums.append(int(''.join(number_extracted)))

                    total += nums[0] * nums[1]

    print('Part 2:', total)


def remove_duplicates(numbers: list) -> list:
    """ Removes duplicated items from a list with dicts

    :param numbers: The dict with duplicates
    :return: The dict without duplicates
    """

    # Convert each dictionary to frozenset, converting lists to tuples
    unique_sets = set(frozenset((k, tuple(v)) for k, v in d.items()) for d in numbers)

    # Convert back to dictionaries
    unique_dicts = [dict(s) for s in unique_sets]

    return unique_dicts


def parse_input(inp:  []) -> dict[int, dict[str, list]]:
    """ Parses the input for the first part.
    Returns a dict with the row index as key and as values the indexes of the numbers and symbols.
    :param inp: The input file as a list
    :return: dict for each row the indexes of the numbers and symbols
    """
    input_parsed = {}
    for index, line in enumerate(inp):
        line = line.strip()
        input_parsed[index] = {
            'numbers': [],
            'symbols': []
        }
        nums = []
        for i, c in enumerate(line):
            if c.isdigit():
                if not nums:
                    nums.append(int(i))
                elif max(nums) + 1 == i:
                    nums.append(int(i))
                else:
                    input_parsed[index]['numbers'].append(nums)
                    nums = [int(i)]
            elif c == '.':
                continue
            else:
                input_parsed[index]['symbols'].append(int(i))

        if nums:
            input_parsed[index]['numbers'].append(nums)
    return input_parsed


def parse_input_part2(inp:  []) -> dict[int, dict[str, list]]:
    """ Parses the input for the second part.
    Returns a dict with the row index as key and as values the indexes of the numbers and symbols.
    The difference to the first part is that only the * is a symbol.
    :param inp: The input file as a list
    :return: dict for each row the indexes of the numbers and symbols
    """
    input_parsed = {}
    for index, line in enumerate(inp):
        line = line.strip()
        input_parsed[index] = {
            'numbers': [],
            'symbols': []
        }
        nums = []
        for i, c in enumerate(line):
            if c.isdigit():
                if not nums:
                    nums.append(int(i))
                elif max(nums) + 1 == i:
                    nums.append(int(i))
                else:
                    input_parsed[index]['numbers'].append(nums)
                    nums = [int(i)]
            elif c == '*':
                input_parsed[index]['symbols'].append(int(i))

        if nums:
            input_parsed[index]['numbers'].append(nums)
    return input_parsed


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == '__main__':
    main()
