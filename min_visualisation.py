import numpy as np
data = np.loadtxt(
    fname= 'data/inflammation-01.csv',
    delimiter = ','
)

min_inflammation = np.min(
    data,
    axix=0
)

ply.plot (min_inflammation)
