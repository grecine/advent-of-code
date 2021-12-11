import pandas as pd
import numpy as np
import time

def input(fname):
    data = []
    with open(fname) as f:
        for line in f:
            l =[l.strip() for l in line.split(' ')]
            data.append([int(x) for x in l[0]])
    data = np.array(data)

    return data        
    
def neighbors(x,x_min,x_max):
    x_nn = []
    x_nn.append([x[0]-1, x[1]  ])
    x_nn.append([x[0]-1, x[1]+1])
    x_nn.append([x[0]  , x[1]+1])
    x_nn.append([x[0]+1, x[1]+1])
    x_nn.append([x[0]+1, x[1]  ])
    x_nn.append([x[0]+1, x[1]-1])
    x_nn.append([x[0]  , x[1]-1])
    x_nn.append([x[0]-1, x[1]-1])
    x_nn = np.array(x_nn)

    x_nn = np.delete(x_nn,np.where(x_nn<x_min)[0], axis=0)
    x_nn = np.delete(x_nn,np.where(x_nn>x_max)[0], axis=0)

    return (tuple(l) for l in x_nn)

class Octopus:
    def __init__(self,octoloc):
        self.octoloc = octoloc
        self.size = self.octoloc.shape[0] * self.octoloc.shape[1]
        self._m = len(octoloc)-1
        self.iter = 0
        self.count = 0
        self.sync = False

    def flashing(self):
        return True if len(np.argwhere(self.octoloc>9)) > 0 else False

    def step(self):
        self.iter += 1

        # Part 1: increase all by 1
        self.octoloc += 1

        # Part 2: increase flashers nn by 1
        while self.flashing():
            flashers = np.argwhere(self.octoloc>9)
            # set to zero if it flashed
            self.octoloc[np.where(self.octoloc>9)] = 0
                
            for f in flashers:
                for x in neighbors(f,0,self._m):
                    if (0 < self.octoloc[x]):
                        self.octoloc[x] = self.octoloc[x] + 1
        
        cnt = len(np.where(oct.octoloc==0)[0])
        self.sync = True if cnt == self.size else False
        self.count += cnt

# fname = 'test-input.txt'
fname = 'input.txt'
check = 100

oct = Octopus(input(fname))

t0 = time.time()
sync = oct.sync
while not sync:
    oct.step()
    if oct.iter == check:
        print('Step '+str(check)+' flash total: '+str(oct.count))
    sync = oct.sync

print('First sync at: '+str(oct.iter))
print('Elapsed time {:.3e}'.format(time.time()-t0)+' sec')