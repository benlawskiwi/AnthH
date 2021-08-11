import numpy as np
import matplotlib.pyplot as plt

init = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
fina = [13,11,10,9,15,14,7,8,4,3,2,18,1,6,5,16,22,12,24,23,21,17,20,19,25]

c,n,d,x,y,z = np.loadtxt('excited.dat',unpack=True)


ca = []
na = []
xa = []
ya = []
za = []
for i in range(0,np.size(init)):
    if init[i] == fina[i]:
        ca.append(c[i])
        na.append(n[i])
        xa.append(x[i])
        ya.append(y[i])
        za.append(z[i])
    if init[i] != fina[i]:
        v = fina[i]-1
        ca.append(c[i])
        na.append(n[i])
        xa.append(-x[v])
        ya.append(y[v])
        za.append(z[v])

fl = np.column_stack((ca,na,d,xa,ya,za))
np.savetxt('flip-excited.dat',fl,delimiter='    ',fmt='%1.0f,%1.0f,%1.0f,%1.7f,%1.7f,%1.7f')
