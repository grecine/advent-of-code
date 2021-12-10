import pandas as pd
import numpy as np
import time


pair = {')': ('(',3), ']': ('[',57), '}': ('{',1197), '>':('<',25137) }
ket = {'(': ')', '[': ']', '{': '}', '<': '>',}
ket_score = {')': 1, ']': 2, '}': 3, '>':4 }

def brak_cnt(line, n):
    cnt = np.array([0,0,0,0,0])
    expected = []
    m = 0
    for c in line:
        cnt+= np.array([1,0,0,0,0]) if c=='(' else np.array([0,0,0,0,0])
        cnt+= np.array([-1,0,0,0,0]) if c==')' else np.array([0,0,0,0,0])
        cnt+= np.array([0,1,0,0,0]) if c=='[' else np.array([0,0,0,0,0])
        cnt+= np.array([0,-1,0,0,0]) if c==']' else np.array([0,0,0,0,0])
        cnt+= np.array([0,0,1,0,0]) if c=='{' else np.array([0,0,0,0,0])
        cnt+= np.array([0,0,-1,0,0]) if c=='}' else np.array([0,0,0,0,0])
        cnt+= np.array([0,0,0,1,0]) if c=='<' else np.array([0,0,0,0,0])
        cnt+= np.array([0,0,0,-1,0]) if c=='>' else np.array([0,0,0,0,0])

        expected.append(ket[c]) if c in '([{<' else expected
        if c in ')]}>':
            if (c != expected[len(expected)-1]) and (m < len(line)):
                cnt[4] = pair[c][1]
                break
            else:
                expected.pop()
        m += 1
    expected.reverse()
    return cnt, expected


# fname = 'test-input.txt'
fname = 'input.txt'
nav_sub = pd.read_csv(fname, sep=',', header=None).iloc[:,0].tolist()

# Part 1
t0 = time.time()
brak_state = np.zeros((len(nav_sub),5))
err_list = []
remaining = []
for n in range(len(nav_sub)):
    brak_state[n], e = brak_cnt(nav_sub[n],n)
    if brak_state[n,4] > 0: err_list.append(n)
    if brak_state[n,4] == 0: remaining.append(e)

print('Part 1:', int(brak_state[:,4].sum()))
print('Part 1 took {:.3e}'.format(time.time()-t0)+' sec')


# Part 2
t0 = time.time()
scores = []
for l in remaining:
    score= 0 
    for k in l:
        score = score*5 + ket_score[k]
    scores.append(score)

print('part 2:',int(np.median(np.array(scores))))
print('Part 2 took {:.3e}'.format(time.time()-t0)+' sec')

