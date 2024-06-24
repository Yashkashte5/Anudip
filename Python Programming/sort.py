import numpy as np
arr = np.array([3,1,2,4,5])

#sort the array in ascending order(creates a new sorted array)
sorted_arr = np.sort(arr)

print ("Sorted array (ascending):",sorted_arr)

sorted_arr_desc = np.sort(arr)[::-1]
print ("Sorted array (descending):",sorted_arr_desc)
