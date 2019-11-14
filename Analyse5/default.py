import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.figure()
plt.plot(xs,ys)
plt.grid(True)

import tikzplotlib

tikzplotlib.save("test.tex")