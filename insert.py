# np.insert(array, index, value, axix)
# axis=0 --> row-wise, axis=1 --> column-wise

import numpy as np

arr=np.array([15, 19, 20, 30, 47, 6])
print(arr)

new_arr=np.insert(arr, 3, 99, axis=0)
print(new_arr)