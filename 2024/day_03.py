import re


def main():
    part_1()
    part_2()


def part_1() -> None:
    """
    Execute Part 1 by calculating and printing the result.

    :return: None
    """
    # Read the input memory
    memory = get_input('./inputs/03_actual.txt')

    # Calculate the result
    count = calculate(memory)

    # Output the result
    print('Part 1:', count)


def part_2() -> None:
    """
    Execute Part 2 by cleaning memory based on skip blocks and calculating the result.

    :return: None
    """

    # Read the input memory
    memory = get_input('./inputs/03_actual.txt')

    # Fet the list of blocks to skip
    skip_blocks = get_skip_blocks(memory)

    # Remove the skip blocks from the memory string
    last_index = 0
    memory_cleaned_parts = []
    for block in skip_blocks:
        memory_cleaned_parts.append(memory[last_index:block[0]])
        last_index = block[1]
    memory_cleaned = ''.join(memory_cleaned_parts)

    # Calculate and print the result
    count = calculate(memory_cleaned)
    print('Part 2:', count)


def calculate(memory: str) -> int:
    """
    Calculate the sum of products from matches of 'mul(a,b)' in the input string.

    :param memory: The input string containing 'mul(a,b)' patterns.
    :return: int: The sum of the products of all matched pairs. Returns 0 if no matches are found.
    """
    re_pattern = r"mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)"
    if matches := re.findall(re_pattern, memory):
        return sum(int(match[0]) * int(match[1]) for match in matches)
    return 0


def get_skip_blocks(memory: str) -> [()]:
    """
    Generate a list of skip blocks based on matches of 'don't()' and 'do()' patterns.
    :param memory: The input string with 'do()' and 'don't()'
    :return: A list of tuples representing skip blocks.
             Each tuple contains the start index
             and the end index (or None if no matching do() is found) of the skip block
    """

    # Find all match positions for "don't()" and "do()"
    matches_stop = [s.end() for s in re.finditer(r"don't\(\)", memory)]
    matches_start = [s.end() for s in re.finditer(r"do\(\)", memory)]

    skip_blocks = []
    last_start = 0

    for stop in matches_stop:
        # Skip stops that are before the last start
        if stop < last_start:
            continue

        # If the stop exceeds the last match start, add it as a final block
        if stop > matches_start[-1]:
            skip_blocks.append((stop, None))
            break

        # Find the first match start that comes after the current stop
        for i, start in enumerate(matches_start):
            if start > stop:
                skip_blocks.append((stop, start))
                # Update matches_start to exclude processed indices
                matches_start = matches_start[i:]
                # Update the last_start to the current start
                last_start = start
                break

    return skip_blocks


def get_input(file_path: str) -> str:
    """
    Reads the content of the given input file and returns it as a single string.

    :param file_path: The path to the input file.
    :return: The content of the file as a single string.
    """

    with open(file_path, 'r') as file:
        return file.read()


if __name__ == '__main__':
    main()
