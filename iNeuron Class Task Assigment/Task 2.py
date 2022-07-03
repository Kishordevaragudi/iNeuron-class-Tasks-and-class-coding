'KISHOR DEVARAGUDI'
#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

# 1 . Try to reverse a list

# 2 . Try to access 234 out of this list

# 3 . Try to access 456

# 4 . Try to extract only a list collection form list l

# 5 . Try to extract "sudh"

# 6 . Try to list all the key in dict element avaible in list

# 7 . Try to extract all the value element form dict available in list

#1 . Try to reverse a list
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
l.reverse()
print(l)

#2 . Try to access 234 out of this list
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
print(l[7][0])

#3 . Try to access 456
print(l[5][1])

#4 . Try to extract only a list collection form list l

indices = [5, 6]
extracted_elements = [l[index] for index in indices]
print(extracted_elements)

#5 . Try to extract "sudh"
print(l[-1]['key1'])

#6 . Try to list all the key in dict element avaible in list
print(l[-1].keys())

#7 . Try to extract all the value element form dict available in list
print(l[-1].values())
