import pandas as pd
import time
import os

decoder = {
    'a': ([0,2,3,5,6,7,8,9], [1,4]),
    'b': ([0,4,5,6,8,9], [1,2,3,7]),
    'c': ([0,1,2,3,4,7,8,9], [5,6]),
    'd': ([2,3,4,5,6,8,9], [0,1,7]),
    'e': ([0,2,6,8], [1,3,4,5,7,9]),
    'f': ([0,1,3,4,5,6,7,8,9], [2]),
    'g': ([0,2,3,5,6,8,9], [1,4,7]),
}

count_map = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0,6,9],
    7: [8],
}

def decode(s, num):
    return s[s.str.len()==num].tolist()

def calc_map(s):

    map = {}

    for num in count_map:
        for i in count_map[num]:
            map[i] = decode(s, num)

    # find 0
    for i in map:
        if len(map[i][0])==5:
            l4 = map[i]
        elif len(map[i][0])==6:
            l5 = map[i]
    for x in l5:
        s = set(l4[0])&set(l4[1])&set(l4[2])&set(x)
        if len(s)==2:
            map[0] = [x]
            map[6].remove(x)
            map[9].remove(x)

    # find 6 & 9
    if len(set(map[6][0]) & set(map[1][0])) == 1:
        map[6] = [map[6][0]]
        map[9].remove(map[6][0])
    else:
        map[6] = [map[6][1]]
        map[9].remove(map[6][0])

    # find 2
    for x in map[2]:
        if len(set(x)&set(map[9][0]))==4:
            map[2] = [x]
            map[5].remove(x)
            map[3].remove(x)

    # find 5 & 3
    if len(set(map[5][0]) & set(map[1][0])) == 1:
        map[5] = [map[5][0]]
        map[3].remove(map[5][0])
    else:
        map[5] = [map[5][1]]
        map[3].remove(map[5][0])

    rev_map = {''.join(sorted(map[i][0])):str(i) for i in map}
    
    return rev_map


# fname = 'test-input.txt'
fname = 'input.txt'

day_dir = os.path.realpath(__file__).split('/')[:-1]
fname = os.path.join('/',*day_dir, fname)
df = pd.read_csv(fname, sep=' ', header=None)

signals = df.loc[:,0:9]
outputs = df.loc[:,11:]

# Part 1
t0 = time.time()
nums = [2,3,4,7]
sum = outputs.apply(lambda col: len(col[col.str.len().isin(nums)]), axis=0).sum()
print('Part 1: '+str(sum)+'\t'+str(time.time()-t0)+' sec')

# Part 2
t0 = time.time()
sum = 0
for idx in signals.index:
    rev_map = calc_map(signals.iloc[idx])
    
    val =''
    for o in outputs.iloc[idx]:
        val += rev_map[''.join(sorted(o))]

    sum += int(val)
    
print('Part 2: '+str(sum)+'\t'+str(time.time()-t0)+' sec')
