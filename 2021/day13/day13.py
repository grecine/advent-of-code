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

def fold_y(A, f):
    max_size = A.shape[1]

    # split
    x_new = A[:,:f]
    for i in range(f+1,max_size):
        x_new[:,2*f-i] = paper[:,i] | paper[:,2*f-i]

    return x_new

def fold_x(A,f):
    max_size = A.shape[0]

    # split
    y_new = A[:f,:]
    for i in range(f+1,max_size):
        y_new[2*f-i,:] = A[i,:] | A[2*f-i,:]

    return y_new

# dots = input('test-input.txt')
dots = input('input.txt')

sep = dots.index('')
folds = [d.split(' ')[2] for d in dots[sep+1:]]
folds = [d.split('=') for d in folds]
# folds = [(d.replace('=',' ')).split(' ')[2:4] for d in dots[sep+1:]]
dots = np.array([list(map(int, d.split(','))) for d in dots[0:sep]])

x_max, y_max = max(dots[:,0]), max(dots[:,1])
paper = np.full((x_max+1,y_max+1),0)
for d in dots:
    paper[tuple(d)] = 1

i = 0
print('#', 'axis', 'num', 'dots', 'shape')
for fold in folds:
    fold_type = fold[0]
    fold_num = int(fold[1])
    fold_op = fold_x if fold_type=='x' else fold_y
    
    paper = fold_op(paper, fold_num)
    print(i, fold_type, fold_num,  paper.sum(), paper.shape)
    i += 1

for line in paper.T:
    print(''.join([str(l).replace('0',' ').replace('1','#') for l in line]))