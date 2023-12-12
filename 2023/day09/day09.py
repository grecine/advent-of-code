import numpy as np
import pandas as pd
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def get_next(hist, series):
    hist = [hist.copy()]

    s = None
    while set(hist[-1]) != {0}:
        s = list(np.diff(hist[-1]))
        hist += [s]

    n = len(series[0]) - len(s) + 1
    hist[-1].append(0)
    for i in range(len(hist) - 1):
        step = n - i - 1
        hist[step - 1].append(hist[step][-1] + hist[step - 1][-1])

    return hist[0][-1]


def get_prev(hist, series):
    hist = [hist.copy()]

    s = None
    while set(hist[-1]) != {0}:
        s = list(np.diff(hist[-1]))
        hist += [s]

    n = len(series[0]) - len(s) + 1
    hist[-1] = [0] + hist[-1]
    for i in range(len(hist) - 1):
        step = n - i - 1
        hist[step - 1] = [-hist[step][0] + hist[step - 1][0]] + hist[step - 1]

    return hist[0][0]


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    series = [list(map(int, data[n].split())) for n in range(len(data))]

    # part 1
    t0 = time.time()
    print('Part 1:')
    print(sum([get_next(x, series) for x in series]))
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    print(sum([get_prev(x, series) for x in series]))
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')


if __name__ == "__main__":
    main()

