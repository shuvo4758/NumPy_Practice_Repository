# np.split(arr, divided part) --> divide into equal part
# np.vsplit()
# np.hsplit()

import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 3))

arr2=np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [1, 2, 3, 4],
              [5, 6, 7, 8],
              ])

print(np.vsplit(arr2, 2))
print(np.hsplit(arr2, 2))