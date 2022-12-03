import numpy as np
import os
import time

np.set_printoptions(threshold=np.inf)

def char2val(c):
    """
    Lowercase item types a through z have values 1 through 26.
    Uppercase item types A through Z have values 27 through 52.
    """
    lowercase_origin=96
    uppercase_origin=38
    if c.isupper():
        return ord(c) - uppercase_origin
    else:
        return ord(c) - lowercase_origin

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
    pri_sum = 0
    for sack in data:
        c1 = sack[0:int(0.5 * len(sack))]
        c2 = sack[int(0.5 * len(sack)):len(sack)]
        common = set(c1) & (set(c2))
        priority = char2val(list(common)[0])
        pri_sum += priority
    #     print(common, priority)
    print(pri_sum)

def part2(data):
    n_groups = int(len(data) / 3)
    pri_sum = 0
    for i in range(n_groups):
        badge = set(data[i * 3]) & set(data[i * 3 + 1]) & set(data[i * 3 + 2])
        priority = char2val(list(badge)[0])
        pri_sum += priority
    #     print(badge)
    print(pri_sum)

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
