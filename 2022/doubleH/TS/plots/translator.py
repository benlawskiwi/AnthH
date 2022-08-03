import numpy as np

#Read in file to rotate

x = np.loadtxt('36-P.cube')

print('Size of x is '+str(np.shape(x)))

xx = []
yy = []
zz = []
V = []

#Create V

for i in range(0,4500):
    for j in range(0,6):
        V.append(x[i,j])

print('Size of V is '+str(np.shape(V)))
#Create indicies

for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            xx.append(i)
            yy.append(j)
            zz.append(k)

print('Size of xx is '+str(np.shape(xx)))
print('Size of yy is '+str(np.shape(yy)))
print('Size of zz is '+str(np.shape(zz)))

#Now to apply transformation
rot = []

for i in range(0,30):
    print('-- '+str(i)+'/30')
    for j in range(0,30):
        for k in range(0,30):
            for l in range(0,np.size(V)):
                if xx[l] == i and zz[l] == j and yy[l] == (29-k):
                    rot.append(V[l])

print('Size of rot is '+str(np.shape(rot)))

#Now to repack data

y = np.zeros((4500,6))

for i in range(0,4500):
    for j in range(0,6):
        ind = i*6+j
        y[i,j] = rot[ind]

print('Size of y is '+str(np.shape(y)))

#Now read in comparison density

z = np.loadtxt('36T.cube')

print('Size of z is '+str(np.shape(z)))

dif = np.zeros((4500,6))

for i in range(0,4500):
    for j in range(0,6):
        dum = y[i,j]-z[i,j]
        if dum < 0:
            dum = 0
        dif[i,j] = '{:.9g}'.format(dum)

print('Size of dif is '+str(np.shape(dif)))

np.savetxt('dif2.cube',dif,fmt='%s',delimiter='  ')
