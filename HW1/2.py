import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi,2*np.pi,0.1)
y = [np.sin(p) for p in x]
y1= [1 for p in x]
plt.plot(x,y)
plt.plot(x,y)
plt.fill_between(x,y,y1)
plt.xlabel("x")
plt.ylabel("y=sin(x)")
plt.show()
