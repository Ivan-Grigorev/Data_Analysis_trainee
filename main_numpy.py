import pandas as pd
import numpy as np


pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)

a = np.array([
    [1, 2, 3],
    [3, 4, 5]
])

b = np.array([
    [6, 7, 8],
    [9, 10, 11],
])

c = np.array([
    [12, 13, 14],
    [15, 16, 17]
])

d = np.arange(10)

e = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

f = np.array([
    [a, b, c, e.__add__(a + b + c)],
    [a, b, c, e.__mul__(a)],
    [a, b, c, e.__truediv__(b - c)]
])

# print(f.ravel(), f.ravel().shape)

# print(d, '\n', d.sum())
# print(a.__truediv__(b + c))

# print(np.copyto(a, b))
# print(f.shape)

# g = f.reshape(3, 8)
# print(g, '\n', g.shape, '\n', f, '\n', f.shape)
# print(np.random.rand(3, 3, 3))

print(np.asarray(b) is b)




