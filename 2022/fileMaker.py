import numpy as np

geo = 2
#step = 0.04874
step = 0.33769

#Read in TS
a,b,c = np.loadtxt('geoIRC/geo-9.txt',delimiter=',',usecols=(1,2,3),unpack=True)
#Read in step
a2,b2,c2 = np.loadtxt('geoIRC/geo-'+str(geo)+'.txt',delimiter=',',usecols=(1,2,3),unpack=True)

#calculate delta
da = (a2-a)/step
db = (b2-b)/step
dc = (c2-c)/step

l = ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','H','H','H','H','H','H','H','H','H','H','H']

#Rxn coordinate to cover
xxx = np.arange(0,0.65,0.05)

for i in range(0,np.size(xxx)):
    x = a-da*xxx[i]
    y = b-db*xxx[i]
    z = c-dc*xxx[i]
    arr = np.column_stack((l,x,y,z))
    serv = '%NProcShared=16\n%mem = 64GB\n%Chk=check_sp_'+str(i)+'\n#n M062X/cc-pvtz TD EmpiricalDispersion=GD3 SP\n \n SP_'+str(i)+'\n\n1 1\n'
    gm=''
    for j in range(0,25):
        gm += '    '+arr[j,0]+'    '+str(arr[j,1])+'    '+str(arr[j,2])+'    '+str(arr[j,3])+'\n'
    fn = 'calcs6b/irc_sp_'+str(i)+'.txt'
    gm += '\n'
    T = serv+gm
    text_file = open(fn,"w")
    text_file.write(T)
    print(T)

