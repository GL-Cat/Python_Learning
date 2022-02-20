import numpy as np

x = np.empty([3,4], dtype = int)
y = [1, 2, 3]
a1 = np.asarray(y, dtype = float)

s = b'Hi frombuffer'
a2 = np.frombuffer(s, dtype='S1')

list = range(5)
z = iter(list)
a3 = np.fromiter(z, dtype=float)

a4 = np.arange(10, 50, 8)

a5 = np.linspace(10, 50, 8, dtype = int)

a6 = np.logspace(0, 4, 6, base = 2)
print(a6)
