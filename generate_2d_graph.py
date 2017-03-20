from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random
import csv

mmax = []
iterations = []
duration = []
headers = []
row_num = 0
matrix_size = 150
with open('report/iterations.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row_num == 0:
            headers = row
            row_num += 1
            continue
        mmax.append(float(row[1]))
        iterations.append(float(row[2]))
        duration.append(float(row[3]))
        row_num += 1

fig, ax = plt.subplots()
ax.scatter(mmax, iterations)
ax.set_title('Mmax vs Iterations to convergence')
ax.set_xlabel('Mmax')
ax.set_ylabel('Iterations')
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
