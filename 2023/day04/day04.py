import numpy as np
import os
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)


def make_cards(data):
    cards = {}
    for d in data:
        n = int(d.split(':')[0].split(' ')[-1])
        nums = d.split(':')[1]
        winning = nums.split('|')[0].strip().split(' ')
        winning = [x for x in winning if x != '']
        mine = nums.split('|')[1].strip().split(' ')
        mine = [x for x in mine if x != '']

        copies = 1

        cards[n] = [winning, mine, copies]

    return cards

def part1(cards):
    total = 0
    for n in cards:
        winning = cards[n][0]
        mine = cards[n][1]

        matches = [x for x in mine if x in winning]
        points = int(2**(len(matches)-1))

        total += points

    print(total)

def part2(cards):
    for n in cards:
        for i in range(cards[n][2]):
            winning = cards[n][0]
            mine = cards[n][1]

            matches = [x for x in mine if x in winning]

            for j in range(len(matches)):
                cards[n+(j+1)][2] += 1

    tot = 0
    for n in cards:
        tot += cards[n][2]

    print(tot)

def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    cards = make_cards(data)

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(cards)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(cards)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

if __name__ == "__main__":
    main()

