import math, time, random
import numpy as np
ntrials=2
dist=0
start_time=time.process_time()
for i in range(ntrials):
    x1=np.random.random()
    y1=np.random.random()
    x2=np.random.random()
    y2=np.random.random()
    dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2))
dist/=ntrials
elapsed_time=time.process_time()-start_time
ex_dist=1/15*(np.sqrt(2)+2+5*np.log(1+np.sqrt(2)))
print("Ntrials=%d  Ave dist=%9.7f  Exact dist=%9.7f Elapsed time=%6.2f"%(ntrials,dist,ex_dist,elapsed_time))