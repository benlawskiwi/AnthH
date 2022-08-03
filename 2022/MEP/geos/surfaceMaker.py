import numpy as np

fn1 = input('Enter frequency number (ie 20): ')
fn1s = 'h6-'+str(fn1)+'.txt'
fn2 = input('Enter frequency number (ie 5): ')
fn2s = 'h6-'+str(fn2)+'.txt'

xx = []
yy = []
zz = []

l = ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','H','H','H','H','H','H','H','H','H','H','H']


#Read in geometry
a,b,c = np.loadtxt('TS.txt',usecols=(0,1,2),unpack=True)
#Read in frequency 1
x1,y1,z1 = np.loadtxt(fn1s,unpack=True)
#Read in frequency 2
x2,y2,z2 = np.loadtxt(fn2s,unpack=True)

#Rxn coordinate to cover
xxx = np.arange(-6,8,2)
yyy = np.arange(-6,8,2)

for i in range(0,np.size(xxx)):
    for j in range(0,np.size(yyy)):
        m = a+x1*xxx[i]/10+x2*yyy[j]/10
        n = b+y1*xxx[i]/10+y2*yyy[j]/10
        o = c+z1*xxx[i]/10+z2*yyy[j]/10
        arr = np.column_stack((l,m,n,o))
        serv = '%NProcShared=48\n%mem = 190GB\n#n M062X/6-311++G(d,p) TD(NStates=1) EmpiricalDispersion=GD3 SP\n \n SP_'+str(xxx[i])+'\n\n1 1\n'
        gm=''
        for k in range(0,25):
            gm += '    '+arr[k,0]+'    '+str(arr[k,1])+'    '+str(arr[k,2])+'    '+str(arr[k,3])+'\n'
        fn = 's'+str(fn1)+'-'+str(fn2)+'/s_sp_'+str(xxx[i])+'_'+str(yyy[j])+'.txt'
        gm += '\n'
        T = serv+gm
        text_file = open(fn,"w")
        text_file.write(T)
        print(T)


#Now write out gaussian command
gauss = '#!/bin/bash\n#PBS -l walltime=10:00:00\n#PBS -l ncpus=48\n#PBS -l mem=190GB\n#PBS -l jobfs=100GB\n#PBS -l software=g16\n#PBS -l wd\n#PBS -P y35\n#PBS -q normal\n\nmodule load gaussian\n'
#print(gauss)
fl = ''
for i in range(0,np.size(xxx)):
    for j in range(0,np.size(yyy)):
         fl += 'g16 < s_sp_'+str(xxx[i])+'_'+str(yyy[j])+'.txt > s_sp_'+str(xxx[i])+'_'+str(yyy[j])+'.out 2>&1\n'

#print(fl)

G = gauss+fl
fn = 's'+str(fn1)+'-'+str(fn2)+'/gauss'+str(fn1)+str(fn2)

text_file = open(fn,"w")
text_file.write(G)
print(G)
