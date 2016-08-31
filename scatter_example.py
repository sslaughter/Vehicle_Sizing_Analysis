'''
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(121)

## the data
N=1000
x = np.random.randn(N)
y = np.random.randn(N)

## left panel
ax1.scatter(x,y,color='blue',s=5,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square


## right panel
ax2 = fig.add_subplot(122)
props = dict(alpha=0.5, edgecolors='none' )

handles = []
colors = ['blue', 'green', 'magenta', 'cyan']
for color in colors:
    x = np.random.randn(N)
    y = np.random.randn(N)
    s = np.random.randint(50,200)
    handles.append(ax2.scatter(x, y, c=color, s=s, **props))

ax2.set_ylim([-5,11])
ax2.set_xlim([-5,11])

ax2.legend(handles, colors)
ax2.grid(True)
ax2.set_aspect(1./ax2.get_data_ratio())
plt.show()

'''

import matplotlib.pyplot as plt
import numpy as np

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

fig, ax = plt.subplots()
num = 1000
s = 121
x1 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
y1 = np.linspace(-5,5,num) + (0.5 - np.random.rand(num))
x2 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
y2 = np.linspace(5,-5,num) + (0.5 - np.random.rand(num))
x3 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
y3 = (0.5 - np.random.rand(num))
ax.scatter(x1, y1, color='r', s=2*s, marker='^', alpha=.4)
ax.scatter(x2, y2, color='b', s=s/2, alpha=.4)
ax.scatter(x3, y3, color='g', s=s/3, marker='s', alpha=.4)
plt.show()