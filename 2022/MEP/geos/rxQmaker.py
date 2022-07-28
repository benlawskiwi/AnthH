import numpy as np

#P
xp,yp,zp = np.loadtxt('P.txt',usecols=(1,2,3),unpack=True)
#R
xr,yr,zr = np.loadtxt('R.txt',usecols=(1,2,3),unpack=True)
#T
xt,yt,zt = np.loadtxt('T.txt',usecols=(1,2,3),unpack=True)

#rxn coord 1 = P-T
x1 = xp-xt
y1 = yp-yt
z1 = zp-zt

#rxn coord 2 = R-T
x2 = xr-xt
y2 = yr-yt
z2 = zr-zt

np.savetxt('h6-R1.txt',np.column_stack((x1,y1,z1)),delimiter='  ')
np.savetxt('h6-R2.txt',np.column_stack((x2,y2,z2)),delimiter='  ')


