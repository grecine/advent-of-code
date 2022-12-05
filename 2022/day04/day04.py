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

data = input('input.txt')
# data = input('test-input.txt')

def part1(data):
    sub_count = 0
    for pair in data:
        elf0 = pair.split(',')[0].split('-')
        elf1 = pair.split(',')[1].split('-')

        elf0 = [i for i in range(int(elf0[0]), int(elf0[1]) + 1)]
        elf1 = [i for i in range(int(elf1[0]), int(elf1[1]) + 1)]

        sub = set(elf0).issubset(elf1) or set(elf1).issubset(elf0)
        sub_count = sub_count + 1 if sub else sub_count

    #     print(elf0 ,elf1, sub)
    #     print(pair, sub)
    print(sub_count)

def part2(data):
    sub_count = 0
    for pair in data:
        elf0 = pair.split(',')[0].split('-')
        elf1 = pair.split(',')[1].split('-')

        elf0 = [i for i in range(int(elf0[0]), int(elf0[1]) + 1)]
        elf1 = [i for i in range(int(elf1[0]), int(elf1[1]) + 1)]

        sub = set(elf0) & set(elf1) != set()
        sub_count = sub_count + 1 if sub else sub_count

    #     print(elf0 ,elf1, sub)
    #     print(pair, sub)
    print(sub_count)
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
