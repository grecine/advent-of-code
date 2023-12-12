import numpy as np
import os
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def build_map(data):
    return np.array([[x for x in d] for d in data])


def expansion(galactic_map, z):
    n_x, n_y = galactic_map.shape

    galaxies = [np.array([i,j]) for i,j in zip(*np.where(galactic_map=='#'))]

    row_insert = np.array([i for i in range(n_x) if set(galactic_map[i,:])=={'.'}])
    col_insert = np.array([i for i in range(n_y) if set(galactic_map[:,i])=={'.'}])

    for n in range(len(galaxies)):
        i, j = galaxies[n][0], galaxies[n][1]

        ii = i + z*len(np.where(row_insert<i)[0])
        jj = j + z*len(np.where(col_insert<j)[0])

        galaxies[n][0] = ii
        galaxies[n][1] = jj

    return galaxies

def distance(g1, g2):
    return sum([abs(i) for i in list(g1-g2)])


def sum_distances(galactic_map, z):
    z = 1 if z==1 else z-1

    galaxies = expansion(galactic_map, z)

    tot = 0
    for n in range(len(galaxies)):
        for g in range(len(galaxies[n+1: ])):
            dist = distance(galaxies[n], galaxies[n+1+g])
            tot += dist

    print(tot)


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    galactic_map = build_map(data)

    # part 1
    t0 = time.time()
    print('Part 1:')
    print(sum_distances(galactic_map, 1))
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    print(sum_distances(galactic_map, int(1E6)))
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')


if __name__ == "__main__":
    main()

