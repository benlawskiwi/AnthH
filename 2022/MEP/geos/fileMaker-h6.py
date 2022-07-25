import numpy as np

fni = input('Enter frequency number (ie 20): ')
fns = 'h6-'+str(fni)+'.txt'

xx = []
yy = []
zz = []

l = ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','H','H','H','H','H','H','H','H','H','H','H']


#Read in geometry
a,b,c = np.loadtxt('T.txt',usecols=(1,2,3),unpack=True)
#Read in frequency
x,y,z = np.loadtxt(fns,unpack=True)

#Rxn coordinate to cover

xxx = np.arange(-5,6,1)

for i in range(0,np.size(xxx)):
    m = a+x*xxx[i]/10
    n = b+y*xxx[i]/10
    o = c+z*xxx[i]/10
    arr = np.column_stack((l,m,n,o))
    serv = '%NProcShared=16\n%mem = 64GB\n%Chk=check_sp_'+str(i)+'\n#n M062X/cc-pvtz TD EmpiricalDispersion=GD3 SP\n \n SP_'+str(xxx[i])+'\n\n1 1\n'
    gm=''
    for j in range(0,25):
        gm += '    '+arr[j,0]+'    '+str(arr[j,1])+'    '+str(arr[j,2])+'    '+str(arr[j,3])+'\n'
    fn = 'f'+str(fni)+'/f_sp_'+str(xxx[i])+'.txt'
    gm += '\n'
    T = serv+gm
    text_file = open(fn,"w")
    text_file.write(T)
    print(T)


#Now write out gaussian command
gauss = '#!/bin/bash\n#PBS -l walltime=8:00:00\n#PBS -l ncpus=16\n#PBS -l mem=64GB\n#PBS -l jobfs=100GB\n#PBS -l software=g16\n#PBS -l wd\n#PBS -P y35\n#PBS -q normal\n\nmodule load gaussian\n'
#print(gauss)
fl = ''
for i in range(0,np.size(xxx)):
    fl += 'g16 < f_sp_'+str(xxx[i])+'.txt > f_sp_'+str(xxx[i])+'.out 2>&1\n'

#print(fl)

G = gauss+fl
fn = 'f'+str(fni)+'/gauss'+str(fni)

text_file = open(fn,"w")
text_file.write(G)
print(G)
