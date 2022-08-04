import numpy as np
import matplotlib.pyplot as plt

#Create Frequency list for each
fr1 = []
for i in range(0,23):
    a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=2+32*i,usecols=(2,3,4),max_rows=1)
    fr1.append(a)
    fr1.append(b)
    fr1.append(c)

fr2 = []
for i in range(0,23):
    a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=2+32*i,usecols=(2,3,4),max_rows=1)
    fr2.append(a)
    fr2.append(b)
    fr2.append(c)


#Create Symmetry list each
sym1 = []
for i in range(0,23):
    a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=1+32*i,usecols=(0,1,2),max_rows=1,dtype='str')
    sym1.append(a)
    sym1.append(b)
    sym1.append(c)

sym2 = []
for i in range(0,23):
    a,b,c = np.loadtxt('h6-TS.txt',unpack=True,skiprows=1+32*i,usecols=(0,1,2),max_rows=1,dtype='str')
    sym2.append(a)
    sym2.append(b)
    sym2.append(c)

#Create matrix from normal mode vectors ---------------- MODE 1 --------------------------------------
#----X----
x1=[]
arrx=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=7+32*i+j,usecols=(4,7,10),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arrx = np.vstack((arrx,ar))
arrx = np.delete(arrx,0,0)
#arrx is (25,69)
#----Y----
x1=[]
arry=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=7+32*i+j,usecols=(2,5,8),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arry = np.vstack((arry,ar))
arry = np.delete(arry,0,0)
#----Z----
x1=[]
arrz=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=7+32*i+j,usecols=(3,6,9),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arrz = np.vstack((arrz,ar))
arrz = np.delete(arrz,0,0)
#Now combine them all
Xarr = np.vstack((arrx,arry,arrz))
#Xarr is (75,69), x1, x2,...z25 - f1, f2, ... f69

#Create matrix from normal mode vectors ---------------- MODE 2 --------------------------------------
x1=[]
arrx2=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=7+32*i+j,usecols=(4,7,10),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arrx2 = np.vstack((arrx2,ar))
arrx2 = np.delete(arrx2,0,0)
#arrx is (25,69)
#----Y----
x1=[]
arry2=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=7+32*i+j,usecols=(2,5,8),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)
    ar = np.array(x1)
    x1 = []
    arry2 = np.vstack((arry2,ar))
arry2 = np.delete(arry2,0,0)
#----Z----
x1=[]
arrz2=np.zeros(69)
for j in range(0,25):
    for i in range(0,23):
        a,b,c = np.loadtxt('h6-GR.txt',unpack=True,skiprows=7+32*i+j,usecols=(3,6,9),max_rows=1)
        x1.append(a)
        x1.append(b)
        x1.append(c)      
    ar = np.array(x1)
    x1 = []
    arrz2 = np.vstack((arrz2,ar))
arrz2 = np.delete(arrz2,0,0)
#Now combine them all
Xarr2= np.vstack((arrx2,arry2,arrz2))
#Xarr is (75,69), x1, x2,...z25 - f1, f2, ... f69

#--------------------------------------------------------
#Now we can start our report!
#freq 1 = i
#freq 2 = j
#atom = k
#--------------------------------------------------------

for i in range(0,69):
    sims = [] #simularity against each other frequency in state 2
    diis = []
    print('Starting Loop # -- '+str(i+1)+'/69')
    for j in range(0,69):
        #print('Starting J # -- '+str(j+1)+'/69')
        sa = []
        da = []
        sb = []
        db = []
        for k in range(0,25):
            #print('Starting Atom # -- '+str(k+1)+'/25')
            v = np.array([arrx[k,i],arry[k,i],arrz[k,i]])
            r = np.array([arrx2[k,j],arrx2[k,j],arrx2[k,j]])
            v_norm = np.sqrt(sum(v**2))
            r_norm = np.sqrt(sum(r**2))
            if v_norm != 0 and r_norm != 0:
                sim_a = np.dot(v,r)/(v_norm*r_norm)
            if v_norm == 0 or r_norm == 0:
                sim_a =0
            di_a = np.sqrt(sum((v-r)**2))
            sa.append(sim_a)
            da.append(da)
            v = v*-1
            v_norm = np.sqrt(sum(v**2))
            r_norm = np.sqrt(sum(r**2))
            if v_norm != 0 and r_norm != 0:
                sim_b = np.dot(v,r)/(v_norm*r_norm)
            if v_norm == 0 or r_norm == 0:
                sim_b =0
            di_b = np.sqrt(sum((v-r)**2))
            sb.append(sim_b)
            db.append(db)
            #print('Ending Atom # -- '+str(k+1)+'/25')
        #print('start of analysis')
        sxa = np.mean(sa)
        sxb = np.mean(sb)
        #print('sx')
        #dxa = np.mean(da)
        #dxb = np.mean(db)
        #print('dx')
        S = max(sxa,sxb)
        #D = min(dxa,dxb)
        #print('S/D')
        sims.append(S)
        #diis.append(D)
        #print('Append')
    xx = max(sims)
    x2 = np.sort(sims)[-2]
    x3 = np.sort(sims)[-3]
    zz = sims.index(max(sims))
    for l in range(0,np.size(sims)):
        if sims[l] == x2:
            z2 = l
        if sims[l] == x3:
            z3 = l
    print('Ground -- '+str(i+1)+'  - '+str(zz+1)+' - '+str(z2+1)+' - '+str(z3+1))

