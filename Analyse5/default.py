import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 6, 100)
Y = np.sin(X)

plt.plot(X,Y)
plt.show()