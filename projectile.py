from matplotlib import pyplot
import numpy as np
angle = np.pi / 3
u = 300
G = -9.8
time = [i/100 for i in range(10000)]
distance = [np.cos(angle) * u * t for t in time]
height = [(np.sin(angle) * u * t) + (G * (t**2) )/2 for t in time]
pyplot.plot(distance, height)
pyplot.show()
