# does not create copy, it returns a view which effects original array
# 1D array to multidimentional array

import numpy as np

arr=np.array([15, 19, 20, 30, 47, 6])

reshaped_arr = arr.reshape(2,3)

print(reshaped_arr)