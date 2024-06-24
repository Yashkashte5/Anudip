import numpy as np
arr = np.array([1,2,3,4,5,6,56,23])

# Split the array into 2 equal sized sub arrays

sub_arrays = np.split(arr,2)
print(type(sub_arrays))
#print the sub-arrays
for sub_arr in sub_arrays:
    print(sub_arr)
