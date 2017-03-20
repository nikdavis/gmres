from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random
import csv

fig = plt.figure()
ax = fig.gca(projection='3d')

x = []
y = []
z = []
headers = []
row_num = 0
with open('generated_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row_num == 0:
            headers = row
            row_num += 1
            continue
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[3]))
        row_num += 1

ax.text2D(0.01, 0.99, "GMRES Performance, Duration", transform=ax.transAxes)
ax.scatter(x, y, z, label='GMRES', cmap='hot')
ax.set_xlabel('Matrix Row, Column Size')
ax.set_ylabel('Iteration / Matrix Size')
ax.set_zlabel('Duration')

plt.show()

# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
#
# mpl.rcParams['legend.fontsize'] = 10
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
#
# plt.show()
