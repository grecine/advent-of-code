import pandas as pd
import numpy as np
import time
import os

def input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/',*day_dir, fname)

    data = []
    with open(fname) as f:
        for line in f:
            data.append(line.strip())
    return data        

def get_cave_map(cave_net):

    cave_net = np.array([c.split('-') for c in cave_net])

    caves = []
    for j in range(cave_net.shape[1]):
        caves.extend(list(set(cave_net[:,j])))
    caves = list(set(caves))

    cave_map = {}
    for cave in caves:  
        ii = np.where(cave_net==cave)
        cave_map[cave] = list(cave_net[ii[0],abs(ii[1])-1])

    small_caves = [c for c in caves if (str.islower(c) and len(c)<3)]

    return cave_map, small_caves

def get_paths(cave_map, small_caves, small_cave_visits):

    visitedList = [[]]

    def go(vertex, visited):
        if str.isupper(vertex):
            res = True
        elif str.islower(vertex):
            lim = 2
            for sc in small_caves:
                if visited.count(sc) == small_cave_visits:
                    lim = 1
            lim = 1 if (vertex=='start' or vertex=='end')  else lim
            res = True if visited.count(vertex) < lim else False
        return res

    def depthFirst(graph, currentVertex, visited):
        visited.append(currentVertex)
        for vertex in graph[currentVertex]:
            if go(vertex, visited):
                depthFirst(graph, vertex, visited.copy())
        visitedList.append(visited)

    depthFirst(cave_map, 'start', [])

    visitedList.remove([])
    paths = []
    for path in visitedList:
        if path[-1] == 'end':
            paths.append(path)

    return paths

cave_net = input('input.txt')
# cave_net = input('test-input.txt')
# cave_net = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end',]

cave_map, small_caves = get_cave_map(cave_net)

t0 = time.time()
paths = get_paths(cave_map, small_caves, 1)
print('Part 1:', len(paths))
print('Part 1 tok {}'.format(time.time()-t0)+' sec')

paths = get_paths(cave_map, small_caves, 2)
print('Part 2:', len(paths))
print('Part 2 tok {}'.format(time.time()-t0)+' sec')
