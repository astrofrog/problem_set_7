# The following function should median-filter the arrays (as in Problem Set 4)
# but it looks like there is an issue in the plot. Why is this?

import numpy as np
np.random.seed(12345)  # ensures the random values are always the same
import matplotlib.pyplot as plt


def median_filter(x, y, width):
    y_new = y
    for i in range(len(x)):
        y_new[i] = np.median(y[(x > x[i] - width * 0.5) &
                               (x < x[i] + width * 0.5)])
    return y_new

n = 1000
x = np.linspace(0., 100., n)
y = 10. * np.cos(x / 10.) + np.random.normal(0., 5., n)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, '.')
ax.plot(x, median_filter(x, y, 5), color='red', lw=3)
fig.savefig('example_4.png')
