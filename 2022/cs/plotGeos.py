import numpy as np
import matplotlib.pyplot as plt

z1,x1,y1 = np.loadtxt('TS.txt',unpack=True)
x2,y2,z2 = np.loadtxt('P.txt',unpack=True)
z3,x3,y3 = np.loadtxt('GR.txt',unpack=True)

for i in range(0,np.size(x1)):
    plt.plot((x3[i],x3[i]),(y3[i],y3[i]),'C2o')
    plt.annotate(str(i+1),(x3[i],y3[i]))
    plt.plot((x2[i],x2[i]),(y2[i]+5,y2[i]+5),'C1o')
    plt.annotate(str(i+1),(x2[i],y2[i]+5))
    plt.plot((x1[i],x1[i]),(y1[i]+9,y1[i]+9),'C0o')
    plt.annotate(str(i+1),(x1[i],y1[i]+9))

plt.show()
