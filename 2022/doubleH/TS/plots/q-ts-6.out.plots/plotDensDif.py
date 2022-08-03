import numpy as np
import matplotlib.pyplot as plt

aa=[]
bb=[]
cc=[]
dd=[]
ee=[]
ff=[]

for j in range(0,1600):
    a,b,c,d,e,f = np.loadtxt('dens.1.cube',skiprows = (31+j*7),max_rows=6,unpack=True)
    a1,b1,c1,d1,e1,f1 = np.loadtxt('dens.E.cube',skiprows = (31+j*7),max_rows=6,unpack=True)
    for i in range(0,np.size(a)):
        aa.append('{:.9g}'.format((a1[i]-a[i])))
        bb.append('{:.9g}'.format((b1[i]-b[i])))
        cc.append('{:.9g}'.format((c1[i]-c[i])))
        dd.append('{:.9g}'.format((d1[i]-d[i])))
        ee.append('{:.9g}'.format((e1[i]-e[i])))
        ff.append('{:.9g}'.format((f1[i]-f[i])))
    a,b,c,d = np.loadtxt('dens.1.cube',skiprows = (31+6+j*7),max_rows=1,unpack=True)
    a1,b1,c1,d1 = np.loadtxt('dens.E.cube',skiprows = (31+6+j*7),max_rows=1,unpack=True)
    aa.append('{:.9g}'.format((a1-a))) 
    bb.append('{:.9g}'.format((b1-b))) 
    cc.append('{:.9g}'.format((c1-c))) 
    dd.append('{:.9g}'.format((d1-d))) 
    ee.append('')
    ff.append('')

print('size of aa = '+str(np.size(aa)))
print('size of ff = '+str(np.size(ff)))
print('Now save as new cube file')

arr = np.column_stack((aa,bb,cc,dd,ee,ff))
np.savetxt('diffE.cube',arr,fmt='%s',delimiter='  ')
