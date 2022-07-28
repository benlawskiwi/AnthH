import numpy as np
import matplotlib.pyplot as plt

height=3.487*2/1.4
width = height/1.4
one_col = (width,height)

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(one_col),gridspec_kw={'height_ratios': [2,1]})

x,y = np.loadtxt('PRT_excited.txt',unpack=True)

ax.plot(x,y,'C1o',markersize='4')

x,y = np.loadtxt('PRT_ground.txt',unpack=True)
ax2.plot(x,y,'C0o',markersize='4')

print('minimum = '+str(min(y)))

ax2.set_ylim(min(y),min(y)+150)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()
d = .015
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
fig.subplots_adjust(left=0.25, bottom=0.05, right=0.95, top=0.95)
plt.xticks([], [])

ax.annotate(r'Potential Energy (cm$^{-1})$',xy=(-5.8, 0.0), rotation=90, xycoords='axes fraction', xytext=(-0.30, 0.2),fontsize=12, ha='center', va='center')
ax2.set_xlabel('IRC Q',fontsize=12)

plt.savefig("fig-plotIRC-PRT.png",dpi=400,bbbox_inches="tight")
plt.show()
