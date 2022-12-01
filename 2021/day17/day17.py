import numpy as np
import os
import time

np.set_printoptions(threshold=np.inf)

def input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/',*day_dir, fname)

    data = []
    with open(fname) as f:
        for line in f:
            data.append(line.strip())
    return data        

# data = input('input.txt')
data = input('test-input.txt')

def part1(data):
    # do stuff
    pass

def part1(data):
    # do stuff
    pass

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