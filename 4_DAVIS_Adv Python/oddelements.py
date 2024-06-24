import numpy as n
arr = n.array([10,2,3,4,5,6,20,45])

#Extract the elements which are odd

odd_elements = n.extract(arr % 2 != 0, arr)
print("Elements that are odd are : ", odd_elements)
