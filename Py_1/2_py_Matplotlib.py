import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = 2 * x + 1
plt.title('Matplotlib test')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x, y)
plt.show()
