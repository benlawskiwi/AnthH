import numpy as np
import matplotlib.pyplot as plt

aa=[]
bb=[]
cc=[]
dd=[]
ee=[]
ff=[]

for j in range(0,900):
    a,b,c,d,e,f = np.loadtxt('dens.3T.cube',skiprows = (31+j*5),max_rows=5,unpack=True)
    a1,b1,c1,d1,e1,f1 = np.loadtxt('dens.3P.cube',skiprows = (31+j*5),max_rows=5,unpack=True)
    print(j)
    for i in range(0,np.size(a)):
        aa.append('{:.9g}'.format((a1[i]-a[i])))
        bb.append('{:.9g}'.format((b1[i]-b[i])))
        cc.append('{:.9g}'.format((c1[i]-c[i])))
        dd.append('{:.9g}'.format((d1[i]-d[i])))
        ee.append('{:.9g}'.format((e1[i]-e[i])))
        ff.append('{:.9g}'.format((f1[i]-f[i])))

print('size of aa = '+str(np.size(aa)))
print('size of ff = '+str(np.size(ff)))
print('Now save as new cube file')

arr = np.column_stack((aa,bb,cc,dd,ee,ff))
np.savetxt('diff36.cube',arr,fmt='%s',delimiter='  ')
