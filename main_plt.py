import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd

from datetime import datetime
# import main_pd


# plt.bar(
#     ['USA', 'China', 'Japan', 'Great Britain'],
#     [5, 21, 26, 3],
#     color=['b', 'r', 'y', 'g']
# )
#
# plt.xlabel('Country', fontsize=20, color='green')
# plt.ylabel('Amount', fontsize=20, color='blue')
# plt.title('Gold medals', fontsize=20)
#
#
# plt.plot(
#     [2061, 2035.8, 2028.5, 2022.5, 2016.4],
#     ['Goverla', 'Brebenskyl', 'Pip_Ivan', 'Petros', 'Gutin_Tomnatik'],
#     label='mountain height',
#     # color=['b', 'r', 'y', 'g', 'orange']
# )

# date = pd.date_range(start=datetime.now().date(), freq='D', periods=7)
# fig, axs = plt.subplots()
# fig, axs = plt.subplots(2, 1)
#
# plt.plot(
#     date,
#     [23, 15, 22, 19, 25, 17, 21],
#     label='day temperature',
#     linestyle='--',
#     marker='D'
# )
# plt.plot(
#     date,
#     [20, 11, 16, 12, 18, 12, 16],
#     label='night temperature',
#     linestyle=':'
# )

# axs.plot(date, [23, 15, 22, 19, 25, 17, 21], label='day temperature')
# axs.plot(date, [20, 11, 16, 12, 18, 12, 16], label='night temperature')
# axs[0].plot(date, [23, 15, 22, 19, 25, 17, 21], label='day temperature')
# axs[1].plot(date, [20, 11, 16, 12, 18, 12, 16], label='night temperature')

# plt.xlabel('Date', fontdict={'size': 15, 'color': 'blue'})
# plt.ylabel('Temperature', fontdict={'size': 15, 'color': 'red'})
# plt.title('Weather', fontdict={'size': 20})
# plt.text(date[0], 15, 'Autumn is normal', fontdict={'color': 'orange'})

# axs[0].set_title('Day', fontsize=10)
# axs[1].set_title('Night', fontsize=10)

# fig.suptitle('Weather', fontsize=15)

# main_pd.date_view.plot()

labels = [
    'Junior Software Engineer',
    'Senior Software Engineer',
    'Software Engineer',
    'System Architect',
    'Technical Lead'
]

# data = [63, 31, 100, 2, 11]
# explode = [0.15, 0, 0, 0, 0]
#
# plt.pie(
#     data,
#     labels=labels,
#     shadow=False,
#     explode=explode,
#     autopct='%.2f%%',
#     pctdistance=5,
#     labeldistance=1
# )

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#
# theta_max = 8 * np.pi
# n = 1000
# theta = np.linspace(0, theta_max, n)
#
# x = theta
# z = np.sin(theta)
# y = np.cos(theta)
#
# ax.plot(x, y, z, 'g')

# plt.legend()

grid = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_surface(x, y, z)

plt.show()

