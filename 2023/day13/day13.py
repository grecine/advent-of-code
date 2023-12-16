import numpy as np
import os
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def part1(data):
    # do stuff
    pass


def part2(data):
    # do stuff
    pass


def main():
    # data = aoctools.utils.read_input('input.txt')
    data = aoctools.utils.read_input('test-input.txt')

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(data)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(data)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')


if __name__ == "__main__":
    main()

