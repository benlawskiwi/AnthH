import numpy as np
import matplotlib.pyplot as plt

n,z,x,y = np.loadtxt('zts6.dat',unpack=True)
n,y,x,z = np.loadtxt('zex6.dat',unpack=True)

cnt = 0
for i in range(0,np.size(x)):
    cnt+=1
    if n[i] == 1:
        lab = str(cnt)+'H'
    if n[i] ==6:
        lab = str(cnt)+'C'
    plt.plot(x[i],y[i],'C0o')
    #plt.annotate(lab,((x[i],y[i])))

cnt = 0
for i in range(0,np.size(x)):
    cnt+=1
    if n[i] == 1:
        lab = str(cnt)+'H'
    if n[i] ==6:
        lab = str(cnt)+'C'
    plt.plot(-x[i],y[i],'C1o',markersize='4')
    #plt.annotate(lab,((x[i],y[i])))

plt.show()
