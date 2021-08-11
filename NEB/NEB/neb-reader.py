import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#fn = input('Enter file name: ')
fn = 'C14H11+test'

x,y = np.loadtxt(fn+'.neb_final_epath',unpack=True)
n = np.size(x)

#f, (ax,ax1) = plt.subplots(2,1)

for i in range(0,n):
    xa=[]
    ya=[]
    za=[]
    skp = 2*(i+1)+25*i
    a,xx,yy,zz = np.loadtxt(fn+'.neb_final.xyz',skiprows=skp,max_rows=25,unpack=True,dtype=str)
    for j in range(0,np.size(xx)):
        if a[j] == 'C':
            xa.append(float(xx[j]))
            ya.append(float(yy[j]))
            za.append(float(zz[j]))
            #print(xx[j])
    #print(xa)
    #print(ya)
    #plt.plot(xa,ya,'o')
    #fig = plt.figure()
    #ax = fig.add_subplot(projection='3d')
    #ax = Axes3D(fig)
    #ax.scatter(xa,ya,za)
    #plt.show()
    f, (ax,ax1) = plt.subplots(2,1)
    ax.plot(xa,za,'o')
    ax.set_xlim(-4,4)
    ax.set_ylim(-0.001,0.001)
    ax1.plot(xa,ya,'o',label=str(i))
    ax1.set_xlim(-4,4)
    ax1.set_ylim(-2,2)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    plt.savefig(fn+str(i)+'.png')
    plt.show()
#plt.legend()
#plt.show()
plt.plot(x,y)
plt.savefig(fn+'_epath.png')
plt.show()
