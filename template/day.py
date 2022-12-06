import numpy as np
import os
import time
import aoc_tools.utils

np.set_printoptions(threshold=np.inf)


def part1(data):
    # do stuff
    pass

def part2(data):
    # do stuff
    pass


def main():
    # data = aoc_tools.utils.read_input('input.txt')
    data = aoc_tools.utils.read_input('test-input.txt')

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(data)
    print('Elapsed time:',time.time()-t0,' sec')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(data)
    print('Elapsed time:',time.time()-t0,' sec')

if __name__ == "__main__":
    main()

