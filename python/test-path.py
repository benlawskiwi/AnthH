import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('test.path',unpack=True)

n = 20
rng = int(np.size(x)/n)
for i in range (rng):
    xx,yy = np.loadtxt('test.path',skiprows=i*n,max_rows=n,unpack=True)
    plt.plot(xx,yy)

plt.show()
