import numpy as np

#Defining 2 arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Concatenating the arrays
concatenated_arr = np.concatenate((arr1, arr2))

print("Concatenated array:", concatenated_arr)

#Mathematical operations
added = concatenated_arr + 2  
subtracted = concatenated_arr - 2  
multiplied = concatenated_arr * 2 
divided = concatenated_arr / 2 
modulo = concatenated_arr % 2 

print("Added 2 to each element:", added)
print("Subtracted 2 from each element:", subtracted)
print("Multiplied each element by 2:", multiplied)
print("Divided each element by 2:", divided)
print("Modulo 2 of each element:", modulo)
