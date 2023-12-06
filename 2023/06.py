import math


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/06_actual.txt')
    time = inp[0].split('Time:')[1].strip().split()
    distance = inp[1].split('Distance:')[1].strip().split()

    record_cnt = []
    for index, t in enumerate(time):
        record_cnt.append(get_number_of_ways(t, distance[index]))

    print('Part 1:', math.prod(record_cnt))


def part_2():
    inp = get_input('./inputs/06_actual.txt')
    time = inp[0].split('Time:')[1].strip().split()
    distance = inp[1].split('Distance:')[1].strip().split()

    time = int(''.join(time))
    distance = int(''.join(distance))

    cnt = get_number_of_ways(time, distance)

    print('Part 2:', cnt)


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


def get_number_of_ways(time, distance) -> int:
    """Calculates the number of ways to win.

    :param time: The total time the race goes
    :param distance: The min distance to beat the record
    :return: The number of ways to beat the record
    """
    time, distance = int(time), int(distance)

    cnt = 0
    for ms in range(time + 1):
        run = time - ms

        run_distance = ms * run
        if run_distance > distance:
            cnt += 1
    return cnt


if __name__ == '__main__':
    main()
