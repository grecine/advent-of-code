import numpy as np
from math import sqrt, floor, ceil
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def parse_line(data, n):
    return [int(x) for x in data[n].split(':')[1].split(' ') if x != '']


def solve_quad(a, b, c):
    k = sqrt(b ** 2 - 4 * a * c)
    return [(-b + k) / (2 * a), (-b - k) / (2 * a)]


def get_min_max(a, b, c):
    x = solve_quad(a, b, c)
    min_x = ceil(min(x) + 1E-10)
    max_x = floor(max(x) - 1E-10)
    return min_x, max_x


def part1(times, distances):
    hold_prod = []
    for t_lim, x_lim in zip(times, distances):
        min_hold, max_hold = get_min_max(1.0, -t_lim, x_lim)
        hold_prod.append(max_hold - min_hold +1)
    print(np.prod(hold_prod))


def part2(times, distances):
    t_lim = int(''.join([str(x) for x in times]))
    x_lim = int(''.join([str(x) for x in distances]))

    min_hold, max_hold = get_min_max(1.0, -t_lim, x_lim)
    print( max_hold - min_hold + 1)


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    times, distances = (parse_line(data, n) for n in [0, 1])

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(times, distances)
    print('Elapsed time:', (time.time() - t0) * 1E3, ' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(times, distances)
    print('Elapsed time:', (time.time() - t0) * 1E3, ' ms')


if __name__ == "__main__":
    main()
