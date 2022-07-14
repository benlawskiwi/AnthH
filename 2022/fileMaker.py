import numpy as np

geo = 2
step = 0.04874

#Read in TS
a,b,c = np.loadtxt('geoIRC/geo-1.txt',delimiter=',',usecols=(1,2,3),unpack=True)
#Read in step
a2,b2,c2 = np.loadtxt('geoIRC/geo-'+str(geo)+'.txt',delimiter=',',usecols=(1,2,3),unpack=True)

#calculate delta
da = (a2-a)/step
db = (b2-b)/step
dc = (c2-c)/step

l = ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','H','H','H','H','H','H','H','H','H','H','H']

#Rxn coordinate to cover
xxx = np.arange(0,1.05,0.05)

for i in range(0,np.size(xxx)):
    x = a-da*xxx[i]
    y = b-db*xxx[i]
    z = c-dc*xxx[i]
    arr = np.column_stack((l,x,y,z))
    serv = '%NProcShared=8\n%mem = 32GB\n%Chk=check_sp_'+str(i)+'\n#n M062X/6-311++G(d,p) TD SP pop=reg formcheck\n \n SP_-'+str(i)+'\n\n1 1\n'
    gm=''
    for j in range(0,25):
        gm += '    '+arr[j,0]+'    '+str(arr[j,1])+'    '+str(arr[j,2])+'    '+str(arr[j,3])+'\n'
    fn = 'calcs2/irc_sp_-'+str(i)+'.txt'
    gm += '\n'
    T = serv+gm
    text_file = open(fn,"w")
    text_file.write(T)
    print(T)

