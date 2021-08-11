import numpy as np
import matplotlib.pyplot as plt

fn = input('Enter file name: ')
F = 69

num = F/3
xt1=[]
xt2=[]
xt3=[]
yt1=[]
yt2=[]
yt3=[]
zt1=[]
zt2=[]
zt3=[]
gap=[]

for i in range(0,23):
    s = 7*(i+1)+25*i
    a,n,x1,y1,z1,x2,y2,z2,x3,y3,z3 = np.loadtxt(fn+'.txt',skiprows=s,max_rows=25,unpack=True)
    for j in range(0,np.size(x1)):
        xt1.append(x1[j])
    for k in range(0,4):
        xt1.append(' ')
    for j in range(0,np.size(x1)):
        xt2.append(x2[j])
    for k in range(0,4):
        xt2.append(' ')
    for j in range(0,np.size(x1)):
        xt3.append(x3[j])
    for k in range(0,4):
        xt3.append(' ')
    for j in range(0,np.size(x1)):
        yt1.append(y1[j])
    for k in range(0,4):
        yt1.append(' ')
    for j in range(0,np.size(x1)):
        yt2.append(y2[j])
    for k in range(0,4):
        yt2.append(' ')
    for j in range(0,np.size(x1)):
        yt3.append(y3[j])
    for k in range(0,4):
        yt3.append(' ')
    for j in range(0,np.size(x1)):
        zt1.append(z1[j])
    for k in range(0,4):
        zt1.append(' ')
    for j in range(0,np.size(x1)):
        zt2.append(z2[j])
    for k in range(0,4):
        zt2.append(' ')
    for j in range(0,np.size(x1)):
        zt3.append(z3[j])
    for k in range(0,4):
        zt3.append(' ')
    for j in range(0,np.size(x1)):
        gap.append('        ')
    for k in range(0,4):
        gap.append('        ')

vec = np.column_stack((gap,xt1,yt1,zt1,gap,xt2,yt2,zt2,gap,xt3,yt3,zt3))
np.savetxt('vec'+fn+'.txt',vec,delimiter=' ',fmt='%s')

flist = []
for i in range(0,23):
    x = np.loadtxt(fn+'.txt',skiprows=(2*(i+1)+30*i),max_rows=1,dtype='str')
    flist.append(x[2])
    #flist.append('  ')
    flist.append(x[3])
    #flist.append('  ')
    flist.append(x[4])
    #flist.append('  ')

np.savetxt('list'+fn+'.txt',flist,delimiter=' ',fmt='%s')

print(flist)

