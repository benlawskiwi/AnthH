import numpy as np
import matplotlib.pyplot as plt

n,x,y,z = np.loadtxt('zex.dat',unpack=True)

cnt = 0
for i in range(0,np.size(x)):
    cnt+=1
    if n[i] == 1:
        lab = str(cnt)+'H'
    if n[i] ==6:
        lab = str(cnt)+'C'
    plt.plot(x[i],y[i],'o')
    plt.annotate(lab,((x[i],y[i])))

plt.show()
