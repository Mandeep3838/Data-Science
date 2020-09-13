import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return x*x*y*y

x = np.arange(-10,10.1,0.1)
y = np.arange(-10,10.1,0.1)

X,Y = np.meshgrid(x,y)
Z = f(X,Y)

fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
