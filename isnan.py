# detects missing values
# np.isnan(arr)

import numpy as np

arr=np.array([1, 2, np.nan, 4, np.nan])

print(np.isnan(arr))

# we can not compare (np.nan == np.nan) directly