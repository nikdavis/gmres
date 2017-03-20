from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random
import csv

matrix_size = []
iteration = []
error_delta = []
duration = []
error_time = []
headers = []
row_num = 0
with open('./report/generated_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row_num == 0:
            headers = row
            row_num += 1
            continue
        matrix_size.append(float(row[0]))
        iteration.append(float(row[1]))
        error_delta.append(float(row[2]))
        duration.append(float(row[3]))
        error_time.append(float(row[4]))
        row_num += 1

x = [
    iteration[:4],
    iteration[4:27],
    iteration[27:76],
    iteration[76:324],
    iteration[324:]
]

y = [
    error_time[:4],
    error_time[4:27],
    error_time[27:76],
    error_time[76:324],
    error_time[324:]
]
fig, ax = plt.subplots()
for i in range(0,5):
    figure = i + 1
    plt.subplot(2, 1, 1)
    print x[i]
    print y[i]
    plt.plot(x[i], y[i])
ax.set_title('Mmax vs Iterations to convergence')
ax.scatter(iteration, error_time, label='GMRES')
ax.set_xlabel('Matrix Row, Column Size')
ax.set_ylabel('Iteration / Matrix Size')
plt.show()
