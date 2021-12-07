import scipy.optimize as opt
import numpy as np
import pandas as pd
import time as time

# cost function
def fuel_used(x, df, part):
    dx = abs(df-x)
    if part==1:
        fuel_used=dx
    elif part==2:
        dx = [int(np.round(x)) for x in dx]
        fuel_used=np.array([np.array([i+1 for i in range(f)]).sum() for f in dx])
    return fuel_used.sum()


# fname = 'test-input.csv'
fname = 'input.csv'

df = np.array(pd.read_csv(fname,header=None).iloc[:,0].tolist())

for p in [1, 2]:
    t0 = time.time()

    res = opt.minimize_scalar(fuel_used, bounds=(df.min(),df.max()), args=(df, p))
    if not res.success:
        print('=====OPTIMIZATION FAILED=====')
        print(res)
    fuel = int(np.round(res.fun))
    pos = int(np.round(res.x))
    print('PART '+str(p))
    print('pos: '+str(pos)+'\tfuel: '+str(fuel))
    print('done in ',str(time.time()-t0),' sec\n')
