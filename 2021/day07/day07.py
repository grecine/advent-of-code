import scipy.optimize as opt
import pandas as pd
import time as time
import os

# cost function
def fuel_used(x, df, part):
    dx = [abs(n-x) for n in df]
    if part==1:
        fuel_used=dx
    elif part==2:
        dx = [int(round(x)) for x in dx] # Fails w/o int only sometimes
        fuel_used=[sum([i+1 for i in range(f)]) for f in dx]
    return sum(fuel_used)


# fname = 'test-input.csv'
fname = 'input.csv'

day_dir = os.path.realpath(__file__).split('/')[:-1]
fname = os.path.join('/',*day_dir, fname)

df = pd.read_csv(fname,header=None).iloc[:,0].tolist()

for p in [1, 2]:
    t0 = time.time()

    res = opt.minimize_scalar(fuel_used, bounds=(min(df),max(df)), args=(df, p))
    if not res.success:
        print('=====OPTIMIZATION FAILED=====')
        print(res)
    fuel = round(res.fun)
    pos = round(res.x)
    print('PART '+str(p))
    print('pos: '+str(pos)+'\tfuel: '+str(fuel))
    print('done in ',str(time.time()-t0),' sec\n')
