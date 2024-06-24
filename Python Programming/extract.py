import numpy as n
arr = n.array([10,2,3,4,5,6,20,45])

#Extract the elements greater than 5

extracted_elements = n.extract(arr > 5, arr)
print("Elements greater than 5 are : ", extracted_elements)
