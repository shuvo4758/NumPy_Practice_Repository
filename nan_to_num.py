# replacing np.nan values by desired number
# np.nan_to_num(arr, nan=Desired_value) --> default value 0

import numpy as np

arr=np.array([1, 2, np.nan, 4, np.nan])

cleaned_arr1=np.nan_to_num(arr)      # default 0
print(cleaned_arr1)

cleaned_arr2=np.nan_to_num(arr, nan=99)      
print(cleaned_arr2)