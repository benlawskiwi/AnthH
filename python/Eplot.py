import numpy as np
import matplotlib.pyplot as plt

e0 = -539.681126523

gx = [-539.681126523,-539.673848066,-539.664520550,-539.672888847,-539.6653886821]
ex = [-539.562929546,-539.569773796,-539.567936930,-539.567936930,-539.5682130850]
lab = ['Ground','Excited','QST2','C$_{2v}$','C$_{s}$']

c = 27.2114

gz = []
ez=[]
for i in range(0,np.size(gx)):
    gz.append((gx[i]-e0)*c)
    ez.append((ex[i]-e0)*c)

xi = []
for i in range(0,np.size(gx)):
    xi.append((i*0.5+i*0.1))

for i in range(0,np.size(gx)):
    plt.plot((xi[i],xi[i]+0.5),(gz[i],gz[i]),'C0')
    plt.plot((xi[i],xi[i]+0.5),(ez[i],ez[i]),'C1')
    plt.annotate(lab[i],(xi[i]+0.25,3.5),ha='center')

plt.ylim(-0.1,3.7)
print(ez)
plt.show()
