import numpy as np
import os
import time

np.set_printoptions(threshold=np.inf)


def stacks_moves(data):
    stack_objs = data[:data.index('') - 1]
    stack_nums = data[data.index('') - 1].strip().split(' ')
    stack_nums = list(filter(lambda a: a != '', stack_nums))
    stack_locs = [data[data.index('') - 1].index(s) for s in stack_nums]

    stacks = []
    for s in stack_locs:
        stack = [l[s] for l in stack_objs]
        stack = list(filter(lambda a: a != ' ', stack))
        stacks.append(stack)

    moves = []
    for m in data[data.index('') + 1:]:
        m = m.split(' ')
        moves.append([m[1], m[3], m[5]])

    return stacks, moves


def input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/', *day_dir, fname)

    data = []
    with open(fname) as f:
        data.extend(line.replace("\n", "") for line in f)
    return data


data = input('input.txt')


# data = input('test-input.txt')

def part1(data):
    stacks, moves = stacks_moves(data)

    for move in moves:
        num = int(move[0])
        source = int(move[1]) - 1
        dest = int(move[2]) - 1

        tmp = [stacks[source].pop(0) for _ in range(num)]
        tmp.reverse()
        tmp.extend(stacks[dest])
        stacks[dest] = tmp

        # print(stacks)

    ans = ''.join([s[0] for s in stacks])

    print(ans)


def part2(data):
    stacks, moves = stacks_moves(data)

    for move in moves:
        num = int(move[0])
        source = int(move[1]) - 1
        dest = int(move[2]) - 1

        tmp = [stacks[source].pop(0) for _ in range(num)]
        #     tmp.reverse()
        tmp.extend(stacks[dest])
        stacks[dest] = tmp

        # print(stacks)

    ans = ''.join([s[0] for s in stacks])

    print(ans)


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
