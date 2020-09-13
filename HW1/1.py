
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,11)
y = [p*p for p in x]

plt.plot(x,y)
plt.fill_betweenx(y,x)
plt.xlabel("x")
plt.ylabel("y=x^2")
plt.show()
