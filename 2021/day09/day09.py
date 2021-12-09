import pandas as pd
import numpy as np


def low(a,i,j):

    if i == 0:
        min = True if a[i+1][j] > a[i][j] else False
    elif i == (a.shape[0]-1):
        min = True if a[i-1][j] > a[i][j] else False
    else:
        min = True if ( (a[i-1][j] > a[i][j]) and 
                        (a[i+1][j] > a[i][j])     ) else False

    if min:
        if j == 0:
            min = True if a[i][j+1] > a[i][j] else False
        elif j == (a.shape[1]-1):
            min = True if a[i][j-1] > a[i][j] else False
        else:
            min = True if ( (a[i][j+1] > a[i][j]) and
                            (a[i][j-1] > a[i][j])     ) else False

    return min   


def flow(x_max, i0, j0, m, n, basin, cave, new_points):
    """ i0, j0: starting coords
        m = element i=0, j=1
        n = increase/decrease +1|-1
    """
    x = [i0,j0]
    prev = cave[tuple(x)]
    basin[tuple(x)]=1
    if n >0:
        down = False if x[m] == x_max[m] else True
    elif n<0:
        down = False if x[m] == 0 else True
    while down:
        x[m] = x[m]+n
        curr = cave[tuple(x)]
        down = prev < curr 
        down = False if curr == 9 else down
        if down:
            basin[tuple(x)] = 1
            new_points.append(tuple(x))
        if n >0:
            down = False if x[m] == x_max[m] else down
        elif n<0:
            down = False if x[m] == 1 else down
        prev = curr

    return basin, new_points


def calc_basin(cave, low_point):

    basin = np.full(cave.shape, 0)
    x_max = (cave.shape[0]-1, cave.shape[1]-1)
    i0 = low_point[0]
    j0 = low_point[1]
    basin[i0,j0]=1
    pts = [[i0,j0]]

    while len(pts)>0:
        i0, j0 = pts.pop(len(pts)-1)
        # find flow points from i0, j0
        basin, pts1 = flow(x_max, i0, j0, 0, +1, basin, cave, pts) # i++
        basin, pts2 = flow(x_max, i0, j0, 0, -1, basin, cave, pts) # i--
        basin, pts3 = flow(x_max, i0, j0, 1, +1, basin, cave, pts) # j++
        basin, pts4 = flow(x_max, i0, j0, 1, -1, basin, cave, pts) # i--
        
    return basin


# fname = 'test-input.txt'
fname = 'input.txt'
cave = np.array(pd.read_csv(fname, sep=',', header=None))

# Part 1
low_points = []
diff = np.full(cave.shape, 0)
for i in range(cave.shape[0]):
    for j in range(cave.shape[1]):
        diff[i][j] = low(cave,i,j)
        if diff[i][j] == 1:
            low_points.append((i,j))

risk = ((cave+1) * diff).sum()

print('Part 1:', risk)


# Part 2
basins = []
sums = []
# for low_point in [low_points[0]]:
for low_point in low_points:
    b = calc_basin(cave, low_point)
    basins.append(b)
    sums.append(b.sum())

total = 1
sums = sorted(sums)
for i in [1,2,3]:
    total *= sums.pop()
print('Part 2',total)
