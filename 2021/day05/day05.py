import numpy as np
import pandas as pd
import os

def path(x0,xf):
    # Vertical line
    if xf[0] == x0[0]:
        line = [(xf[0], y) for y in range(min(x0[1],xf[1]),max(x0[1],xf[1])+1)]
    
    # Non-vertical line
    else:
        m = (xf[1]-x0[1])/(xf[0]-x0[0])
        b = x0[1] - m*x0[0]

        y = lambda x: int(m*x+b)

        line = [(x,y(x)) for x in range(min(x0[0],xf[0]),max(x0[0],xf[0])+1)]
            
    return line

def solve(vents, part):
    n = vents.max()+1
    grid = np.zeros((n,n))

    for line in vents:
        x0 = (line[0], line[1])
        xf = (line[2], line[3])
        if part==1:
            if (x0[0]==xf[0]) or (x0[1]==xf[1]):
                for i,j in path(x0,xf):
                    grid[j][i] += 1
        elif part==2:
            for i,j in path(x0,xf):
                grid[j][i] += 1
        else:
            print("No such part")

    print(len(np.where(grid > 1)[0]))


# fname = 'test-input.csv'
fname = 'input.csv'

day_dir = os.path.realpath(__file__).split('/')[:-1]
fname = os.path.join('/',*day_dir, fname)

vents = pd.read_csv(fname).values

solve(vents, 1)

solve(vents, 2)
