import numpy as np
import os
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def part1(data):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible = []
    for game in data:
        num, turns = game.split(':')[0], game.split(':')[1]
        num = int(num.split(' ')[-1])
        turns = [{y.split(' ')[2]: int(y.split(' ')[1]) for y in x.split(',')} for x in turns.split(';')]
        possible.append(num)
        i = 0
        for balls in turns:
            imp = True if True in [balls[c] > max_cubes[c] for c in balls] else False
            if (num in possible) and imp:
                possible.remove(num)
            i += 1

    print(np.sum(possible))


def part2(data):
    powers = []
    for game in data:
        num, turns = game.split(':')[0], game.split(':')[1]
        num = int(num.split(' ')[-1])
        turns = [{y.split(' ')[2]: int(y.split(' ')[1]) for y in x.split(',')} for x in turns.split(';')]

        i = 0
        max_red = max_green = max_blue = 0
        for balls in turns:
            max_red = max(max_red, balls['red']) if 'red' in balls else max_red
            max_green = max(max_green, balls['green']) if 'green' in balls else max_green
            max_blue = max(max_blue, balls['blue']) if 'blue' in balls else max_blue
            i += 1
        power = max_red * max_green * max_blue
        powers.append(power)

    print(np.sum(powers))


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

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

