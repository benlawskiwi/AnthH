import numpy as np
import matplotlib.pyplot as plt

c,n,d,x,y,z = np.loadtxt('excited.dat',unpack=True)

cnt = 0
for i in range(0,np.size(x)):
    cnt+=1
    if n[i] == 1:
        lab = str(c[i])+'H'
    if n[i] ==6:
        lab = str(c[i])+'C'
    plt.plot(x[i],y[i],'o')
    plt.annotate(lab,((x[i],y[i])))

plt.show()
