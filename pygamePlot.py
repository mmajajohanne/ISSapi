
# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)


# plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot')
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, 1, 2, 1)
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])
ax.set_zlim([-1, 4])
plt.show()

#plan
# create the figure
fig = plt.figure()

# add axes
ax = fig.add_subplot(111,projection='3d')

xx, yy = np.meshgrid(range(10), range(10))
z = (9 - xx - yy) / 2 

# plot the plane
ax.plot_surface(xx, yy, z, alpha=0.5)

plt.show()