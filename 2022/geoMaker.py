import numpy as np

xx = []
yy = []
zz = []
#select geometry
geo = 2

#First row
a,b,c = np.loadtxt('IRC.txt',skiprows=geo,usecols=(4,5,6),unpack=True,max_rows=1,delimiter=',')
xx.append(a)
yy.append(b)
zz.append(c)

#Now main text
for i in range(0,14):
    a,b,c,d,e = np.loadtxt('IRC.txt',skiprows=geo+10*(i+1),usecols=(2,3,4,5,6),unpack=True,max_rows=1,delimiter=',')
    if i%3 == 1:
        zz.append(a)
        xx.append(b)
        yy.append(c)
        zz.append(d)
        xx.append(e)
    if i%3 == 2:
        yy.append(a)
        zz.append(b)
        xx.append(c)
        yy.append(d)
        zz.append(e)
    if i%3 == 0:
        xx.append(a)
        yy.append(b)
        zz.append(c)
        xx.append(d)
        yy.append(e)

#Now last row
a,b = np.loadtxt('IRC.txt',skiprows=geo+10*15,usecols=(2,3),unpack=True,max_rows=1,delimiter=',')
yy.append(a)
zz.append(b)

l = ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','H','H','H','H','H','H','H','H','H','H','H']

arr = np.column_stack((l,xx,yy,zz))

fn = 'geoIRC/geo-'+str(geo)+'.txt'
np.savetxt(fn,arr,fmt="%s",delimiter = ',')

print('geometry #'+str(geo)+' is wirrten!')

#print(np.size(l))
#print(np.size(xx))
#print(np.size(yy))
#print(np.size(zz))
#print(xx)
#print(yy)
#print(zz)
