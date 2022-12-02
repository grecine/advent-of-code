import numpy as np
import os
import time

np.set_printoptions(threshold=np.inf)

decoder1 = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

decoder2 = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

win_scores = {'Lose': 0, 'Draw': 3, 'Win': 6}


def rpss(turn):
    them = turn[0]
    you = turn[1]
    if you == them:
        return 'Draw'
    elif you == 'Rock':
        res = 'Win' if them == 'Scissors' else 'Lose'
        return res
    elif you == 'Paper':
        res = 'Win' if them == 'Rock' else 'Lose'
        return res
    elif you == 'Scissors':
        res = 'Win' if them == 'Paper' else 'Lose'
        return res


def rpss_inv(turn):
    them = turn[0]
    res = turn[1]
    if res == 'Draw':
        return them
    elif res == 'Win':
        if them == 'Rock': return 'Paper'
        if them == 'Paper': return 'Scissors'
        if them == 'Scissors': return 'Rock'
    elif res == 'Lose':
        if them == 'Rock': return 'Scissors'
        if them == 'Paper': return 'Rock'
        if them == 'Scissors': return 'Paper'


def input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/',*day_dir, fname)

    data = []
    with open(fname) as f:
        for line in f:
            data.append(line.strip())
    return data        

data = input('input.txt')
# data = input('test-input.txt')

def part1(data):
    guide = []
    for i in data:
        l = tuple(i.split())
        guide.append([decoder1[l[0]], decoder1[l[1]]])

    total_score = 0
    for r in guide:
        res = rpss(r)
        score = win_scores[res] + shape_scores[r[1]]
        total_score += score
    print(total_score)

def part2(data):
    guide = []
    for i in data:
        l = tuple(i.split())
        guide.append([decoder2[l[0]], decoder2[l[1]]])

    total_score = 0
    for r in guide:
        res = rpss_inv(r)
        score = win_scores[r[1]] + shape_scores[res]
        total_score += score
    print(total_score)

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
