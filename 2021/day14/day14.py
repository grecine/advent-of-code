import pandas as pd
import numpy as np
import time

np.set_printoptions(threshold=np.inf)

def input(fname):
    data = []
    with open(fname) as f:
        for line in f:
            data.append(line.strip())
    return data        

def count_ele(pairs):
    elem_count = {e: 0 for e in rules.values()}
    for pair in pairs:
        elem_count[pair[0][0]] += 0.5*pair[1]
        elem_count[pair[0][1]] += 0.5*pair[1]
    
    elem_count[seed[0]] += 0.5
    elem_count[seed[-1]] += 0.5
    return elem_count

def do_steps(pairs, rules, n):
    for i in range(n):
        new_pairs = []
        for pair in pairs:
            insertion = rules[pair[0]]
            new_pairs.extend([(pair[0][0]+insertion, pair[1]), (insertion+pair[0][1], pair[1])]) 

        counts = {p: 0 for p in set(np.array(new_pairs)[:,0])}
        for n in new_pairs:
            counts[n[0]] += n[1]
        pairs = [(p, counts[p]) for p in counts]

        elem_count = count_ele(pairs)
    
    min_ele = min(elem_count, key=elem_count.get)
    max_ele = max(elem_count, key=elem_count.get)
    print(int(elem_count[max_ele] - elem_count[min_ele]))

# rules = input('test-input.txt')
rules = input('input.txt')
seed = rules[0]
rules = {d.split(' ')[0]: d.split(' ')[2] for d in rules[2:]}

unique_pairs = set([seed[i]+seed[i+1] for i in range(len(seed)-1)])
pairs = [(p, list(unique_pairs).count(p)) for p in unique_pairs]

t0 = time.time()
print('Part 1:')
do_steps(pairs, rules, 10)
print('Elapsed time:',time.time()-t0,' sec')

t0 = time.time()
print('\nPart 2:')
do_steps(pairs, rules, 40)
print('Elapsed time:',time.time()-t0,' sec')