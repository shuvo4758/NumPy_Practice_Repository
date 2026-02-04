import numpy as np

arr_2d = np.array([[1, 2, 3], 
                  [4, 5, 6]])

print(arr_2d)

new_arr_2d_row = np.insert(arr_2d, 1, [7, 8, 9], axis=0)
print(new_arr_2d_row)

new_arr_2d_col = np.insert(arr_2d, 1, [10, 11], axis=1)
print(new_arr_2d_col)

new_arr_2d_none = np.insert(arr_2d, 1, [20, 30, 40], axis=None)
print(new_arr_2d_none)