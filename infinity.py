# inf means infinity which exceed python number limit
# 10^10000 or divided by 0

import numpy as np

arr=np.array([1, 2, np.inf, 4, -np.inf])

print(np.isinf(arr))

cleaned_arr=np.nan_to_num(arr, posinf=1000, neginf=-1000)   # pos=positive infinity
print(cleaned_arr)