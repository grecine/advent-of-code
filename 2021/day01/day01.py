import pandas as pd
import time

# fname = 'test-input.csv'
fname = 'input.csv'

df = pd.read_csv(fname, header=None)

t0 = time.time()
print('Part 1:'+str([df[df.diff()>0].count()][0])+'\t'+str(time.time()-t0)+' sec')

t0 = time.time()
print('Part 2:'+str(df[df.rolling(3).sum().diff()>0].count()[0])+'\t'+str(time.time()-t0)+' sec')