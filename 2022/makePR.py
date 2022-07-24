import numpy as np

za,zb,zc = np.loadtxt('prodReact.txt',usecols=(3,4,5),unpack=True)

xt = []
yt = []
zt = []

for i in range(0,np.size(za)):
    if i%3 == 0:
        xt.append(za[i])
    if i%3 == 1:
        yt.append(za[i])
    if i%3 == 2:
        zt.append(za[i])

xr = []
yr = []
zr = []

for i in range(0,np.size(za)):
    if i%3 == 0:
        xr.append(zb[i])
    if i%3 == 1:
        yr.append(zb[i])
    if i%3 == 2:
        zr.append(zb[i])

xp = []
yp = []
zp = []

for i in range(0,np.size(za)):
    if i%3 == 0:
        xp.append(zc[i])
    if i%3 == 1:
        yp.append(zc[i])
    if i%3 == 2:
        zp.append(zc[i])

l = ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','H','H','H','H','H','H','H','H','H','H','H']

arrt = np.column_stack((l,xt,yt,zt))
arrr = np.column_stack((l,xr,yr,zr))
arrp = np.column_stack((l,xp,yp,zp))

serv = '%NProcShared=16\n%mem = 64GB\n%Chk=check_sp_'+str(i)+'\n#n M062X/cc-pvtz TD EmpiricalDispersion=GD3 SP\n \n SP_'+str(i)+'\n\n1 1\n'

arr = np.column_stack((l,xt,yt,zt))
gm='' 
for j in range(0,25):   
    gm += '    '+arr[j,0]+'    '+str(arr[j,1])+'    '+str(arr[j,2])+'    '+str(arr[j,3])+'\n'
fn = 'calcs6/irc_sp_T.txt'
gm += '\n'
T = serv+gm
text_file = open(fn,"w")
text_file.write(T)
print(T)

arr = np.column_stack((l,xr,yr,zr))
gm=''     
for j in range(0,25):     
    gm += '    '+arr[j,0]+'    '+str(arr[j,1])+'    '+str(arr[j,2])+'    '+str(arr[j,3])+'\n'
fn = 'calcs6/irc_sp_R.txt'
gm += '\n'
T = serv+gm
text_file = open(fn,"w")
text_file.write(T)
print(T)

arr = np.column_stack((l,xp,yp,zp))
gm=''     
for j in range(0,25):     
    gm += '    '+arr[j,0]+'    '+str(arr[j,1])+'    '+str(arr[j,2])+'    '+str(arr[j,3])+'\n'
fn = 'calcs6/irc_sp_P.txt'
gm += '\n'
T = serv+gm
text_file = open(fn,"w")
text_file.write(T)
print(T)
