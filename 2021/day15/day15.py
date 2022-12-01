import numpy as np
import os
import time
# I'm cheating -- I'll write my own A* later
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
# from pathfinding.finder.a_star import AStarFinder as Finder # 47s
# from pathfinding.finder.best_first import BestFirst as Finder # WRONG
# from pathfinding.finder.bi_a_star import BiAStarFinder as Finder # 20s
# from pathfinding.finder.ida_star import IDAStarFinder as Finder # FAILED
# from pathfinding.finder.msp import MinimumSpanningTree as Finder # FAILED
from pathfinding.finder.breadth_first import BreadthFirstFinder as Finder # WRONG

np.set_printoptions(threshold=np.inf)

def input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/',*day_dir, fname)

    data = []
    with open(fname) as f:
        for line in f:
            data.append(line.strip())
    return data        

def find_path(matrix):
    grid = Grid(matrix=matrix)

    start = grid.node(0,0)
    end = grid.node(matrix.shape[0]-1,matrix.shape[1]-1)

    # finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    finder = Finder(diagonal_movement=DiagonalMovement.never)
    path, _runs = finder.find_path(start, end, grid)

    # print('operations:', _runs, 'path length:', len(path))
    # print(grid.grid_str(path=path, start=start, end=end))

    return path

def expand_map(risk_map, r):
    big_map = np.zeros((risk_map.shape[0]*r,risk_map.shape[1]*r))

    n = risk_map.shape[0]

    big_map[0:n,0:n] = risk_map
    for i in range(1,r):
        big_map[0:n,i*n:(i+1)*n] = big_map[0:n,(i-1)*n:i*n]+1
        big_map[np.where(big_map>9)] = 1
    for i in range(1,r):
        big_map[i*n:(i+1)*n,0:n*r] = big_map[(i-1)*n:i*n,0:n*r]+1
        big_map[np.where(big_map>9)] = 1
    return big_map

def total_risk(path, risk_map):
    sum = 0
    for p in path:
        sum += risk_map[p[1],p[0]]
    return sum - risk_map[0,0]

def part1(data):
    path = find_path(data)
    print('Part 1: '+str(total_risk(path,data)))

def part2(data):
    m = 5
    big_map = expand_map(data,m)
    path = find_path(big_map)
    print('Part 2: '+str(total_risk(path,big_map)))

data = input('input.txt')
# data = input('test-input.txt')
data = np.array([[int(i) for i in d] for d in data])

# part 1
t0 = time.time()
part1(data)
print('Elapsed time:',time.time()-t0,' sec')

# part 2
t0 = time.time()
part2(data)
print('Elapsed time:',time.time()-t0,' sec')