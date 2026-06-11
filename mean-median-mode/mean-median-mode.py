import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean=np.mean(x)
    median=np.median(x)
    d = {}
    for i in x:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    mode=max(d.keys(),key=d.get)
    t=(mean,median,mode)
    return t
    pass
