import numpy as np
import os
import re
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)
this_dir = os.path.realpath(__file__).split('/')[:-1]

def get_first_last(text):
    first = re.search(r"\d", text)
    last = re.search(r"\d", text[::-1])

    first = first if first is None else first.start()
    last = last if last is None else last.start() + 1

    return first, last


def part1(data):
    tot = 0
    for s in data:
        f, l = get_first_last(s)
        tot += int(s[f] + s[-l])
    print(tot)

def part2(data):
    matches = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    tot = 0
    for s in data:
        x = [([i.start() for i in re.finditer(x, s)], x) for x in matches]
        x = [(min(n[0]), n[1]) for n in x if n[0]!=[]]
        f_loc = (1E10, None)
        for n in x:
            f_loc = (n[0], n[1]) if n[0] < f_loc[0] else f_loc

        x = [([i.start() for i in re.finditer(x[::-1], s[::-1])], x) for x in matches]
        x = [(min(n[0]), n[1]) for n in x if n[0]!=[]]
        l_loc = (1E10, None)
        for n in x:
            l_loc = (n[0], n[1]) if n[0] < f_loc[0] else l_loc

        f, l = get_first_last(s)

        if f is None:
            first = matches[f_loc[1]]
            last = matches[l_loc[1]]
        else:
            first = matches[f_loc[1]] if f_loc[0] < f else s[f]
            last = matches[l_loc[1]] if l_loc[0] < l else s[-l]

        tot += int(first+last)

    print(tot)

def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input(os.path.join('/', *this_dir, 'test-input.txt'))

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

