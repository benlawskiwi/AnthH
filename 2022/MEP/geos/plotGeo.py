import numpy as np
import matplotlib.pyplot as plt
import glob
import os

#minimum
ts = 539.712106

#Grid Size
step = 0.1
istep = 2
istart = -20
istop = 20

isa = np.arange(istart,istop+istep,istep)
sa = isa/10
print(sa)

geo = input('Enter frequency mode to plot (ie 6): ')
path = 'f'+str(geo)+'/'

string1 = 'Total Energy'
string2 = 'Excited State   1'

ee = []
cc = []
gg = []

for filename in glob.glob(os.path.join(path, '*.out')):
    #print(filename)
    a = filename.split('_')[2].split('.')[0]
    b = int((float(a) - float(istart))/istep)
    c = sa[b]
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
    cc.append(c)
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

cc = np.array(cc)
ee = np.array(ee)
gg = np.array(gg)
ind = np.argsort(cc)
cs = cc[ind]
es = ee[ind]
gs = gg[ind]

np.savetxt(path+'z_'+str(geo)+'PES.txt',np.column_stack((cs,es)))
np.savetxt(path+'y_'+str(geo)+'PES.txt',np.column_stack((cs,gs)))

plt.plot(cs,es,'o')
plt.xlabel('Coordinate Qn')
plt.ylabel('Wavenumbers cm$^{-1}$')
plt.show()

plt.plot(cs,gs,'o')
plt.xlabel('Coordinate Qn')
plt.ylabel('Wavenumbers cm$^{-1}$')
plt.show()
