def main():
    part_1()
    part_2()


def part_1():
    reports = get_input('./inputs/02_actual.txt')
    count = sum(1 for report in reports if is_linear(report, False))
    print('Part 1:', count)


def part_2():
    reports = get_input('./inputs/02_actual.txt')
    count = sum(1 for report in reports if is_linear(report, True))
    print('Part 2: ', count)


def is_linear(report: [int], problem_dampener: bool) -> bool:
    """
    Check if the numbers in the report form a linear progression (increasing or decreasing).
    A linear progression is when the differences between numbers is between 1 and 3.

    If 'problem_dampener' is set to True, one number in the report can be out of the order.

    :param report: A list of integers
    :param problem_dampener: A flag that allows one number to be out of order.
    :return: True if the report is linear
    """

    def check_linear(differences: [int]) -> bool:
        """Check if the differences indicate a linear progression."""
        increasing = all(d > 0 and 3 >= d >= 1 for d in differences)
        decreasing = all(d < 0 and 3 >= abs(d) >= 1 for d in differences)
        return increasing or decreasing

    if not problem_dampener:
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        return check_linear(differences)

    # Handle the case with problem_dampener enabled
    if is_linear(report, False):
        return True

    for index in range(len(report)):
        report_with_removed_element = report[:index] + report[index + 1:]
        if is_linear(report_with_removed_element, False):
            return True

    return False


def get_input(file_path: str) -> list[list[int]]:
    """
    Read a file and parse its contents into a list of lists of integers.
    """

    result = []
    with open(file_path, 'r') as file:
        for line in file:
            result.append([int(num) for num in line.split()])
    return result


if __name__ == '__main__':
    main()
