import numpy as np
import matplotlib.pyplot as plt

fn = input('Enter filename (excited): ')

n,a,d,x,y,z = np.loadtxt(fn+'.dat',unpack=True)
np.savetxt(fn+'.csv',np.column_stack((a,x,y,z)),delimiter=',',fmt='%1.0f, %1.5f, %1.5f, %1.5f')

#Now lets look at the structure
print('Spread of z: '+str(np.mean(abs(z))))
print('Spread of y: '+str(np.mean(abs(y))))
print('Spread of x: '+str(np.mean(abs(x))))

xx=[]
yy=[]
zz=[]
xx2=[]
yy2=[]
for i in range(0,np.size(n)):
    if a[i] == 1: continue
    xx.append(x[i])
    xx2.append(-x[i])
    yy.append(y[i])
    yy2.append(-y[i])
    zz.append(z[i])

aa = []
for i in range(0,np.size(n)):
    if a[i] == 1:
        aa.append('H')
    if a[i] == 6:
        aa.append('C')
xa=[]
xm=[]
ya=[]
za=[]
for i in range(0,np.size(n)):
    xa.append('{:.7f}'.format(x[i]))
    xm.append('{:.7f}'.format(-x[i]))
    ya.append('{:.7f}'.format(y[i]))
    za.append('{:.7f}'.format(z[i]))

np.savetxt(fn+'flop.csv',np.column_stack((xx,zz)),delimiter=',',fmt='%1.8f')
np.savetxt(fn+'mirror.txt',np.column_stack((aa,xm,ya,za)),fmt="%s",delimiter='    ')
np.savetxt(fn+'initial.txt',np.column_stack((aa,xa,ya,za)),fmt="%s",delimiter='    ')

f, (ax,ax1) = plt.subplots(2,1)
ax.plot(xx,zz,'o')
ax.set_xlim(-4,4)
ax.set_ylabel('z')
ax1.plot(xx,yy,'o')
ax1.set_xlim(-4,4)
ax1.set_ylim(-2,2)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
plt.savefig(fn+'.png')
#plt.plot(yy2,zz,'o')
plt.show()
