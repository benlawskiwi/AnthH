import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib import cm
import os

#minimum
ts = 539.712106

#Grid Size
xxx = np.arange(-6,8,2)
yyy = np.arange(-6,8,2)


geo1 = input('Enter first frequency mode to plot (ie 20): ')
geo2 = input('Enter second frequency mode to plot (ie 0): ')
path = 's'+str(geo1)+'-'+str(geo2)+'/'

string1 = 'Total Energy'
string2 = 'Excited State   1'

ee = []
aa = []
bb = []
gg = []

for filename in glob.glob(os.path.join(path, '*.out')):
    print(filename)
    #inda = filename.split('_')[2].split('-')[0]
    #indb = filename.split('_')[2].split('-')[1].split('.')[0]
    inda = filename.split('_')[2]
    indb = filename.split('_')[3].split('.')[0]
    inda = (int(inda)+6)/2
    indb = (int(indb)+6)/2
    print(inda)
    print(indb)
    stpa = (xxx[int(inda)])/10
    stpb = (yyy[int(indb)])/10
    fn = open(filename,'r')
    index = 0
    flag = 0
    for line in fn:
        index += 1
        if string1 in line:
            flag = 1
            break
    x = np.loadtxt(filename,skiprows=(index-1),max_rows=1,unpack=True,dtype='str')
    e = (float(x[4])+ts)*219474.6
    aa.append(stpa)
    bb.append(stpb)
    ee.append(e)
    index = 0
    flag = 0
    fn = open(filename,'r')
    for line in fn:
        index += 1
        if string2 in line:
            flag = 1
            break
    x = np.loadtxt(filename,skiprows=(index-1),max_rows=1,unpack=True,dtype='str')
    et = float(x[4])
    eg = e-et*8065.74
    gg.append(eg)


aa = np.array(aa)
print(aa)
bb = np.array(bb)
ee = np.array(ee)
gg = np.array(gg)
#ind1 = np.argsort(bb)
#aa = aa[ind1]
#bb = bb[ind1]
#ee = ee[ind1]
#gg = gg[ind1]
#ind2 = np.argsort(aa)
#aa = aa[ind2]
#bb = bb[ind2]
#ee = ee[ind2]
#gg = gg[ind2]

np.savetxt(path+'z_'+str(geo1)+'-'+str(geo2)+'PES.txt',np.column_stack((aa,bb,ee)))
#np.savetxt(path+'y_'+str(geo)+'PES.txt',np.column_stack((cs,gs)))

zzz = np.zeros((np.size(yyy),np.size(xxx)))
X,Y = np.meshgrid(xxx,yyy)

for i in range(0,np.size(yyy)):
   for j in range(0,np.size(xxx)):
       ay = yyy[i]/10
       ax = xxx[j]/10
       for k in range(0,np.size(aa)):
           if aa[k] == ax and bb[k] == ay:
               az = ee[k]
       zzz[i,j] = az

print('--------------Matrix sizes-----------------')
print('Size aa = '+str(np.shape(aa)))
print('Size bb = '+str(np.shape(bb)))
print('Size ee = '+str(np.shape(ee)))
print('Size xxx = '+str(np.shape(xxx)))
print('Size yyy = '+str(np.shape(yyy)))
print('Size zzz = '+str(np.shape(zzz)))
print('Size X = '+str(np.shape(X)))
print('Size Y = '+str(np.shape(Y)))
#contour plot
h = plt.contourf(xxx,yyy,zzz,levels=15)
plt.xlabel('Q_'+str(geo1))
plt.ylabel('Q_'+str(geo2))
plt.show()

#surface plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(Y,X,zzz, cmap=cm.coolwarm)
plt.xlabel('Q_'+str(geo1))
plt.ylabel('Q_'+str(geo2))
#ax.axes.set_zlim3d(bottom=12000, top=13000)
plt.show()


#plt.plot(cs,es,'o')
#plt.xlabel('Coordinate Qn')
#plt.ylabel('Wavenumbers cm$^{-1}$')
#plt.show()

#plt.plot(cs,gs,'o')
#plt.xlabel('Coordinate Qn')
#plt.ylabel('Wavenumbers cm$^{-1}$')
#plt.show()
