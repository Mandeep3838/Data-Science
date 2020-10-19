
import numpy as np

import matplotlib.pyplot as plt

def f(x,y):
    return x*x - y*y

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x,y)

Z = f(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,cmap='viridis',edgecolor='none')
ax.set_title('Contour Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
# ax.set_zlabel('x^2-y^2')
plt.show()