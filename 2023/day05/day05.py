import numpy as np
from tqdm.auto import tqdm
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def make_map(data):
    keys = [
        'seeds',
        'seed-to-soil map',
        'soil-to-fertilizer map',
        'fertilizer-to-water map',
        'water-to-light map',
        'light-to-temperature map',
        'temperature-to-humidity map',
        'humidity-to-location map',
    ]

    seeds = tmp = []
    for x in data:
        tmp.extend(x.split(':'))
    tmp = [x.strip() for x in tmp if x != '']

    key_indexes = [tmp.index(k) for k in keys]
    new_map = {}
    for i in range(len(key_indexes)):
        ikey = key_indexes[i]
        ibeg = key_indexes[i]+1
        iend = key_indexes[i+1] if i+1 < len(key_indexes) else None
        if tmp[ikey] == 'seeds':
            seeds = [int(i.strip()) for i in tmp[ibeg:iend][0].split(' ')]
        else:
            new_map[tmp[ikey]] = tmp[ibeg:iend]

    for k in new_map:
        for i in range(len(new_map[k])):
            l = new_map[k][i].split(' ')
            rng = int(l[2])
            dest = int(l[0])
            src = int(l[1])
            new_map[k][i] = [dest, src, rng]

    keys.remove('seeds')

    return seeds, keys, new_map


def do_map(n, k, elf_map):
    m = elf_map[k]
    mapped_n = n
    for l in m:
        dest = l[0]
        src = l[1]
        rng = l[2]
        if src <= n < src+rng:
            mapped_n = dest + (n-src)

    return mapped_n


def part1(seeds, keys, elf_map):
    location = []
    for s in seeds:
        n = s
        for k in keys:
            n = do_map(n, k, elf_map)
        location.append(n)

    print(min(location))


def part2(seeds, keys, elf_map):
    location = []
    for i in range(int(len(seeds)/2)):
        n = seeds[2*i]
        for k in keys:
            n = do_map(n, k, elf_map)
        location.append((n,i))

    min_loc = min(location)[0]
    i = min(location)[1]

    new_seeds = [seeds[2*i]+j for j in range(seeds[2*i+1])]

    for s in tqdm(new_seeds):
        n = s
        for k in keys:
            n = do_map(n, k, elf_map)
        min_loc = min(min_loc, n)

    print(min_loc)


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    seeds, keys, elf_map = make_map(data)

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(seeds, keys, elf_map)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(seeds, keys, elf_map)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

if __name__ == "__main__":
    main()

