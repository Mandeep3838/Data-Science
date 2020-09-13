import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return x*x*y*y

x = np.arange(-10,10.1,0.1)
y = np.arange(-10,10.1,0.1)

X,Y = np.meshgrid(x,y)
Z = f(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x,Y,Z,cmap='viridis',edgecolor='none')
ax.set_title('Surface Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('(xy)^2')
plt.show()
