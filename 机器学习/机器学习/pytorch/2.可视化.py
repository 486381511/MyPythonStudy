import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10,83,1)
y = np.cos(x)
y1 = np.sin(x)
plt.plot(x,y)
plt.plot(x,y1)
plt.title('sinx&cosx')
plt.show()




