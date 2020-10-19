
import numpy as np

import matplotlib.pyplot as plt 
import random

x = np.arange(-5,6)
y = np.arange(-5,6)

p_24 = []

for i in range(24):
    p_24.append([x[random.randint(0,len(x)-1)],y[random.randint(0,len(y)-1)]])
    # y_24.append(y[random.randint(0,len(y)-1)])

p_24 = np.array(p_24)
print(p_24)

from scipy.spatial import ConvexHull, convex_hull_plot_2d
hull = ConvexHull(p_24)

# print(hull.simplices)

plt.plot(p_24[:,0], p_24[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(p_24[simplex, 0], p_24[simplex, 1], 'k-')

plt.title('Convex Hull')

plt.show()

