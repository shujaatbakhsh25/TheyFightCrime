import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4 * np.pi, 4 * np.pi, 0.01)

y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, x, z)

plt.show()
