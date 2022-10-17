import matplotlib.pyplot as plt
import numpy as np


x = np.array([i for i in range(1000)][::-1])
y = np.array([i for i in range(1000)])
z = np.array([i for i in range(1000)])

plt.plot(x, y, z, '_')
plt.show()