import numpy as np
import pandas as pd
import time
import aoctools.utils

np.set_printoptions(threshold=np.inf)

card_map = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

hand_types = {
    'Five of a kind': 7,
    'Four of a kind': 6,
    'Full house': 5,
    'Three of a kind': 4,
    'Two pair': 3,
    'One pair': 2,
    'High card': 1
}

def part1(hands, pt2=False):
    rank = []
    hand = []
    for h, b in hands:
        unique_cards = list(set(h))
        cnt = [h.count(x) for x in unique_cards]

        if pt2 and ('J' in unique_cards) and (max(cnt)<5):
            v = cnt.pop(unique_cards.index('J'))
            cnt[cnt.index(max(cnt))] += v

        if max(cnt) == 5:
            score = hand_types['Five of a kind']
        elif max(cnt) == 4:
            score = hand_types['Four of a kind']
        elif max(cnt) == 3:
            score = hand_types['Full house'] if min(cnt) == 2 else hand_types['Three of a kind']
        elif max(cnt) == 2:
            score = hand_types['Two pair'] if cnt.count(2) == 2 else hand_types['One pair']
        else:
            score = hand_types['High card']

        hand = {i+1: [card_map[h[i]]] for i in range(len(h))}
        hand['bet'] = [int(b)]
        hand['score'] = [int(score)]
        rank.append(pd.DataFrame(hand))

    df = pd.concat(rank).sort_values(['score', 1, 2, 3, 4, 5]).reset_index(drop=True)
    df['winnings'] = (df.index + 1)*df['bet']
    print(df['winnings'].sum())


def part2(hands):
    part1(hands, True)


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    hands = [(x.split(' ')[0], x.split(' ')[1]) for x in data]

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(hands)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(hands)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

if __name__ == "__main__":
    main()

