import numpy as np
import matplotlib.pyplot as plt

#Create Frequency list
fr = []
for i in range(0,23):
    a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=2+32*i,usecols=(2,3,4),max_rows=1)
    fr.append(a)
    fr.append(b)
    fr.append(c)

#Create Symmetry list
sym = []
for i in range(0,23):
    a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=1+32*i,usecols=(0,1,2),max_rows=1,dtype='str')
    sym.append(a)
    sym.append(b)
    sym.append(c)


#Create matrix from normal mode vectors

x1=[]
arrx=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=7+32*i+j,usecols=(4,7,10),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arrx = np.vstack((arrx,ar))

#print(arrx)
arrx = np.delete(arrx,0,0)
#print('Size of x1 array')
#print(np.shape(arrx))

#Now repeat for y 

x1=[]
arry=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=7+32*i+j,usecols=(2,5,8),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arry = np.vstack((arry,ar))

#print(arry)
arry = np.delete(arry,0,0)

#Now repeat for z

x1=[]
arrz=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=7+32*i+j,usecols=(3,6,9),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arrz = np.vstack((arrz,ar))

#print(arrz)
arrz = np.delete(arrz,0,0)

Xarr = np.vstack((arrx,arry,arrz))
#print('Size of total array x,y,z')
#print(np.shape(Xarr))

#Matrixing complete!
#Next code comes from convertRxn.py

#Read in correct data
#skiprows = i+1 and i+9

xx = []
yy = []
zz = []

#First do 2 original rows
s1,e1,r1,x1,y1,z1 = np.loadtxt('h6-IRC.txt',unpack=True,skiprows=9,max_rows=1)
s2,e2,r2,x2,y2,z2 = np.loadtxt('h6-IRC.txt',unpack=True,skiprows=1,max_rows=1)
xx.append(x2-x1)
yy.append(y2-y1)
zz.append(z2-z1)

for i in range(1,15):
    s1,e1,r1,x1,y1,z1 = np.loadtxt('h6-IRC.txt',unpack=True,skiprows=(18*i+9),max_rows=1)
    s2,e2,r2,x2,y2,z2 = np.loadtxt('h6-IRC.txt',unpack=True,skiprows=(18*i+1),max_rows=1)
    if (i+2)%3 ==0:
        xx.append(e2-e1)
        yy.append(r2-r1)
        zz.append(x2-x1)
        xx.append(y2-y1)
        yy.append(z2-z1)
    if (i+1)%3 ==0:
        zz.append(e2-e1)
        xx.append(r2-r1)
        yy.append(x2-x1)
        zz.append(y2-y1)
        xx.append(z2-z1)
    if i%3 ==0:
        yy.append(e2-e1)
        zz.append(r2-r1)
        xx.append(x2-x1)
        yy.append(y2-y1)
        zz.append(z2-z1)
#Now do final 2 rows
s1,y1,z1 = np.loadtxt('h6-IRC.txt',unpack=True,skiprows=279,max_rows=1)
s2,y2,z2 = np.loadtxt('h6-IRC.txt',unpack=True,skiprows=271,max_rows=1)
yy.append(y2-y1)
zz.append(z2-z1)

#xx *= 1/0.38970
#yy *= 1/0.38970
#zz *= 1/0.38970

print('THIS IS THE REACTION VECTOR')
vec = np.column_stack((xx,yy,zz))
print(vec)
#print(np.shape(vec))

#make one vertical array
ar = xx+yy+zz
Yarr = np.array(ar)
Yarr *=1/0.38540
#print('Size of answer array')
#print(np.shape(Yarr))



#---------------------------------------------------------------
#Now matrices are set we can start new calculations
#i 0->69 = mode
#j 0->25 = atom
#v = arrx,arry,arrz
#r = vec
#-------------------------------------------------------------

sarr = []
darr = []
rnarr = []
rnX = 0.032004177852274225
print('Here is the report')

for i in range(0,69):
    sims = []
    dis = []
    for j in range(0,25):
        v = np.array([arrx[j,i],arry[j,i],arrz[j,i]])
        r = np.array([vec[j,0],vec[j,1],vec[j,2]])
        v_norm = np.sqrt(sum(v**2))
        r_norm = np.sqrt(sum(r**2))
        sim_a = np.dot(v,r)/(v_norm*r_norm)
        if v_norm == 0:
            sim_a =0
        di_a = np.sqrt(sum((v-r)**2))
        sims.append(sim_a*r_norm/rnX)
        dis.append(di_a*r_norm/rnX)
        rnarr.append(r_norm)
    s_a = np.mean(sims)
    d_a = np.mean(dis)
    sims = []
    dis = []
    for j in range(0,25):
        v = np.array([arrx[j,i],arry[j,i],arrz[j,i]])
        v = v*-1
        r = np.array([vec[j,0],vec[j,1],vec[j,2]])
        v_norm = np.sqrt(sum(v**2))
        r_norm = np.sqrt(sum(r**2))
        sim_b = np.dot(v,r)/(v_norm*r_norm)
        if v_norm == 0:
            sim_b = 0
        di_b = np.sqrt(sum((v-r)**2))
        sims.append(sim_b*r_norm/rnX)
        dis.append(di_b*r_norm/rnX)
    s_b = np.mean(sims)
    d_b = np.mean(dis)
    S = max(s_a,s_b)
    D = min(d_a,d_b)
    sarr.append(S)
    darr.append(D)
    print('Freq mode: '+str(i+1)+' Frequency: '+str(fr[i])+' Cosine Sim: '+str(S)+' Euc. Dist. '+str(D))
print('Maximum R_Norm: '+str(max(rnarr)))

for i in range(0,69):
    if sym[i] == 'A1':
        plt.plot((fr[i],fr[i]),(0,sarr[i]),'C0')
        plt.annotate(str(i+1),(fr[i],sarr[i]),color='C0')
    if sym[i] == 'A2':
        plt.plot((fr[i],fr[i]),(0,sarr[i]),'C2')
        plt.annotate(str(i+1),(fr[i],sarr[i]),color='C2')
    if sym[i] == 'B1':
        plt.plot((fr[i],fr[i]),(0,sarr[i]),'C1')
        plt.annotate(str(i+1),(fr[i],sarr[i]),color='C1')
    if sym[i] == 'B2':
        plt.plot((fr[i],fr[i]),(0,sarr[i]),'C3')
        plt.annotate(str(i+1),(fr[i],sarr[i]),color='C3')
plt.plot((0,0),(0,0),'C0',label='A1')
plt.plot((0,0),(0,0),'C2',label='A2')
plt.plot((0,0),(0,0),'C1',label='B1')
plt.plot((0,0),(0,0),'C3',label='B2')
plt.legend()
plt.xlabel('Mode Frequency')
plt.ylabel('Cosine Sim. wrt Rxn Coord.')

plt.show()

for i in range(0,69):
    if sym[i] == 'A1':
        plt.plot((fr[i],fr[i]),(0,darr[i]),'C0')
        plt.annotate(str(i+1),(fr[i],darr[i]),color='C0')
    if sym[i] == 'A2':
        plt.plot((fr[i],fr[i]),(0,darr[i]),'C2')
        plt.annotate(str(i+1),(fr[i],darr[i]),color='C2')
    if sym[i] == 'B1':
        plt.plot((fr[i],fr[i]),(0,darr[i]),'C1')
        plt.annotate(str(i+1),(fr[i],darr[i]),color='C1')
    if sym[i] == 'B2':
        plt.plot((fr[i],fr[i]),(0,darr[i]),'C3')
        plt.annotate(str(i+1),(fr[i],darr[i]),color='C3')
plt.plot((0,0),(0,0),'C0',label='A1')
plt.plot((0,0),(0,0),'C2',label='A2')
plt.plot((0,0),(0,0),'C1',label='B1')
plt.plot((0,0),(0,0),'C3',label='B2')
plt.legend()
plt.xlabel('Mode Frequency')
plt.ylabel('Euclid. Dist. from Rxn Coord.')

plt.show()











#Now we can try and solve the problem using lin.algebra
#X C = Y

C = np.linalg.lstsq(Xarr,Yarr)
print(C[0])
print(np.shape(C[0]))

con = C[0]

#Now print in a useable form
n = []
f = []
co = []

for i in range(0,np.size(con)):
    if abs(con[i]) >= 1e-2:
        n.append(i+1)
        co.append(con[i])
        f.append(fr[i])

final = np.column_stack((n,f,co))
print('Final answer - n, f, co')
print(final)
np.savetxt('h6-Matrix.txt',final,fmt='%1.0f    %1.2f       %1.2f')
