import numpy as n
arr = n.array([10,2,3,4,5,6,20,45])

#Extract the elements greater than 10

extracted_elements = n.extract(arr > 10, arr)
print("Elements greater than 10 are : ", extracted_elements)
