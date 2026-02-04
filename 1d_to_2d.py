# broadcasting in 1d array to 2d array

import numpy as np

matrix=np.array([[1, 2, 4, 5],
                 [7, 8, 9, 3]
                 ])     # 2*4 matrix
vector=np.array([10, 20, 30, 40])
result=matrix+vector
print(result)