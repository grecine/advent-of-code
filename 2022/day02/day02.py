import numpy as np
import os
import time
import aoc_tools.utils

np.set_printoptions(threshold=np.inf)

rpss = aoc_tools.utils.rpss()

decoder1 = {
    'A': rpss.rock,
    'B': rpss.paper,
    'C': rpss.scissors,
    'X': rpss.rock,
    'Y': rpss.paper,
    'Z': rpss.scissors
}

decoder2 = {
    'A': rpss.rock,
    'B': rpss.paper,
    'C': rpss.scissors,
    'X': rpss.lose,
    'Y': rpss.draw,
    'Z': rpss.win
}

shape_scores = {rpss.rock: 1, rpss.paper: 2, rpss.scissors: 3}

win_scores = {rpss.lose: 0, rpss.draw: 3, rpss.win: 6}


def part1(data):
    guide = []
    for i in data:
        line = tuple(i.split())
        guide.append([decoder1[line[0]], decoder1[line[1]]])

    total_score = 0
    for r in guide:
        res = rpss.play(r)
        score = win_scores[res] + shape_scores[r[1]]
        total_score += score
    print(total_score)


def part2(data):
    guide = []
    for i in data:
        line = tuple(i.split())
        guide.append([decoder2[line[0]], decoder2[line[1]]])

    total_score = 0
    for r in guide:
        res = rpss.play_inv(r)
        score = win_scores[r[1]] + shape_scores[res]
        total_score += score
    print(total_score)


def main():
    data = aoc_tools.utils.read_input(os.path.join(os.getcwd(), 'input.txt'))
    # data = aoc_tools.utils.read_input(os.path.join(os.getcwd(),'input.txt'))

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(data)
    print('Elapsed time:', time.time() - t0, ' sec')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(data)
    print('Elapsed time:', time.time() - t0, ' sec')


if __name__ == "__main__":
    main()
