import numpy as np
import matplotlib.pyplot as plt


width = 3.487*2
#height = width/1.618 #golden ratio
height = width/1.4
one_col = (width, height*2)
fig,ax = plt.subplots(figsize=one_col)

#P
yp,zp,xp = np.loadtxt('P.txt',usecols=(1,2,3),unpack=True)
#R
xr,yr,zr = np.loadtxt('R.txt',usecols=(1,2,3),unpack=True)
#T
yt,zt,xt = np.loadtxt('T.txt',usecols=(1,2,3),unpack=True)
#TS
xts,yts,zts = np.loadtxt('TS.txt',usecols=(0,1,2),unpack=True)

#rxn coord 1 = P-T
x1 = xp-xt
y1 = yp-yt
z1 = zp-zt

#rxn coord 2 = R-T
x2 = xr-xt
y2 = yr-yt
z2 = zr-zt

#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#First plot 3 geometries
for i in range(0,25):
    #ax.plot(xt[i],yt[i],zt[i],'C0o',markersize=14)
    #ax.plot(xr[i],yr[i],zr[i],'C1o',markersize=14)
    if i < 14:
        plt.plot(yt[i],zt[i],'C2o')
        plt.arrow(yts[i],zts[i]+7,y1[i]*20,z1[i]*20,width=0.002,head_width=0.10,color='k')
        plt.plot(yts[i],zts[i]+7,'C1o')
    if i > 13:
        plt.plot(yt[i],zt[i],'C2o',markersize='3')
        plt.arrow(yts[i],zts[i]+7,y1[i]*20,z1[i]*20,width=0.002,head_width=0.10,color='k')
        plt.plot(yts[i],zts[i]+7,'C1o',markersize='3')
    #plt.annotate(str(i),(yt[i],zt[i]),color='C0')
    #plt.annotate(str(i),(yts[i],zts[i]+6),color='C1')

plt.legend(loc=1,fontsize=10,frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.yticks([])
#plt.xticks([0,2000,4000,6000,8000])
#ax.set_xticklabels(['0','2000','4000','6000','8000'],fontsize=14)
#plt.minorticks_on()
#plt.xlabel('Excitation Energy (cm$^{-1}$)',fontsize=14)
ax.tick_params(width=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)

plt.savefig('fig-molPlot-PRT.png', dpi=600,bbox_inches='tight')

plt.show()
