from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# as plot_surface needs 2D arrays as input
x = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
y = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
     0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
# we make a meshgrid from the x,y data
X, Y = np.meshgrid(x, y)
Z = np.zeros(shape=(len(y), len(x)))
for i, a in enumerate(y):
    for j, b in enumerate(x):
        if a <= 0.1:
            Z[i][j] = 2 * a
        elif a > 0.1 and a <= 0.3:
            Z[i][j] = a + 0.1
        elif a > 0.3 and a <= 0.5:
            Z[i][j] = a + 0.1
        elif a > 0.5 and a <= 0.7:
            Z[i][j] = a + 0.1
        elif a > 0.7:
            Z[i][j] = a + 0.1

# plot_surface with points X,Y,Z and data_value as colors
surf = ax.plot_surface(X, Y, Z, cmap='Greys', antialiased=True)

plt.show()
