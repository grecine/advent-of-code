import numpy as np
import pandas as pd
import time as time

def go_fish(fname):
    fish = np.array(pd.read_csv(fname).iloc[:,0].tolist())

    # Initalize fish counts
    fish_counts = np.zeros(9)
    for n in fish:
        fish_counts[n]+=1

    return fish_counts
    
def evolve(fish_counts, days):
    # Evolve
    for i in range(days):
        new = fish_counts[0]
        fish_counts = np.roll(fish_counts,-1)
        fish_counts[8] = new
        fish_counts[6] += new

    return int(fish_counts.sum())


# fname = 'test-input.csv'
fname = 'input.csv'

fish_dist = go_fish(fname)

# Part 1
t0 = time.time()
days=80
print(days,'days:',evolve(fish_dist, days))

dt = time.time()-t0
print("done in",dt/1E-6,"µs")

# Part 2
t0 = time.time()
days=256
print(days,'days:',evolve(fish_dist, days))

dt = time.time()-t0

print("done in",dt/1E-6,"µs")
