import numpy as np
import matplotlib as plt

data = np.loadtxt(
    fname='data/inflammation-01.csv',
    delimiter=','
)
ave_inflammation = np.mean(
     data,
     axis=0
)

plt.plot (ave_inflammation)

ave_inflammation = np.max(
     data,
     axis=0
)

plt.plot (ave_inflammation)
