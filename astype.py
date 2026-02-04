import numpy as np 

arr=np.array([1.2, 3.6, 7.5])
print("Before conversion : ")
print(arr)

int_arr=arr.astype(int)

print("After conversion : ")
print(int_arr)
