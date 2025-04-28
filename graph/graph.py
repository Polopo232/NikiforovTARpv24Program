import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-12, 12 + 0.1, 0.1)
y1 = -1/18 * x1**2 + 12

x2 = np.arange(-4, 4 + 0.1, 0.1)
y2 = -1/8 * x2**2 + 6

x3 = np.arange(-12, -4 + 0.1, 0.1)
y3 = -1/8 * (x3 + 8)**2 + 6

x4 = np.arange(4, 12 + 0.1, 0.1)
y4 = -1/8 * (x4 - 8)**2 + 6

x5 = np.arange(-4, -0.3 + 0.1, 0.1)
y5 = 2 * (x5 + 3)**2 - 9

x6 = np.arange(-4, 0.2 + 0.1, 0.1)
y6 = 1.5 * (x6 + 3)**2 - 10

plt.plot(x1, y1, label='1')
plt.plot(x2, y2, label='2')
plt.plot(x3, y3, label='3')
plt.plot(x4, y4, label='4')
plt.plot(x5, y5, label='5')
plt.plot(x6, y6, label='6')

plt.title('')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()