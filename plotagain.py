# from pylab import *
#
# from numpy import *
# x = linspace(0, 5, 10)
# y = x ** 2
#
# figure()
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('title')
#
# subplot(1,2,1)
# plot(x, y, 'r--')
# subplot(1,2,2)
# plot(y, x, 'g*-');
import matplotlib.pyplot as plt
from pylab import *
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

plt.show()
