marks=[23,53,52,75,67]
for i in marks:
    print(i)
    
print("The number of items in 'marks' are : ",len(marks))

#Add element at the end
marks.append(45)
print(marks)

#add element at the specific index location
marks.insert(2,60)
print(marks)

#Remove element from the list
marks.remove(23)
print(marks)