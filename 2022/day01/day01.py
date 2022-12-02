import numpy as np
import os
import time

np.set_printoptions(threshold=np.inf)


def get_input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/', *day_dir, fname)

    data = []
    with open(fname) as f:
        for line in f:
            data.append(line.strip())
    return data


def make_sums(data):
    elf_calories = []
    el = []
    for line in data:
        line = line.strip()
        if line == '':
            elf_calories.append(el)
            el = []
        else:
            el.append(int(line))

    elf_sum = [sum(e) for e in elf_calories]
    elf_sum.sort()

    return [elf_sum[len(elf_sum) - (i + 1)] for i in range(3)]


input_data = get_input('input.txt')
# input_data = get_input('test-input.txt')


def part1(data):
    top_3 = make_sums(data)
    print(f"Part 1 answer: {top_3[0]}")


def part2(data):
    top_3 = make_sums(data)
    print(f"Part 1 answer: {sum(top_3)}")


# part 1
t0 = time.time()
print('Part 1:')
part1(input_data)
print('Elapsed time:', time.time() - t0, ' sec')

# part 2
t0 = time.time()
print('\nPart 2:')
part2(input_data)
print('Elapsed time:', time.time() - t0, ' sec')
