String = 'iNeuron'
for i in range(0, 4):
    for j in range(0, i + 1):
        print(String, end=' ')
    print()

# Question 2

rows = 2
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("i ", end="")
    print("")

k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("i ", end="")
    print("")

#List is given to answer further questions
l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']]

#Question 3: Extracting all list entities
for i in l:
  if type(i) == list:
    for j in i:
      print(j)

#Question 4: Extracting all Dictionary Entities
for i in l:
  if type(i) == dict:
    for k,v in i.items():
      print(k,":",v)

#Question 5: Extracting all tuple entities
for i in l:
  if type(i) == tuple:
    for j in i:
      print(j)


#Question 6: Extracting all the numerical data
l2 = []
for i in l:
  if type(i) == int:
    l2.append(i)
  if type(i) == list or type(i) == tuple:
    for j in i:
      if type(j) == int:
        l2.append(j)
  if type(i) == dict:
    for k,v in i.items():
      if type(k) == int or type(v) == int:
        l2.append(k)
        l2.append(v)
print(l2)

#Question 7: Extracting summation of all numerical data
sum = sum(l2)
print(sum)

#Question 8: Filter out all the odd values out of the numerical data
l2_odd = []
for i in l2:
  if i % 2 != 0:
   l2_odd.append(i)

print(l2_odd)

#Question 9: Extract 'ineuron' out of the data
l
l3 = []
for i in l:
  if type(i) == list or type(i) == tuple:
    for j in i:
      if j == 'ineuron':
        l3.append(j)
  if type(i) == dict:
    for k,v in i.items():
      if k == 'ineuron':
        l3.append(k)
      if v == 'ineuron':
        l3.append(v)
print(l3)
#Question 10: Number of Occurences of all the data
l2

def CountOccurrence(a):
  k = {}
  for j in a:
    if j in k:
      k[j] +=1
    else:
      k[j] =1
  return k

print(CountOccurrence(l2))

#Question 11: Number of keys in Dictionary element
l
count = 0
for i in l:
  if type(i) == dict:
    for key,value in i.items():
      count += 1

print(count)
#Question 12: Filter out the String Data
l3 = []
for i in l:
  if type(i) == int:
    l3.append(i)
  if type(i) == str:
    l3.append(i)
  if type(i) == list or type(i) == tuple:
    for j in i:
      l3.append(j)
  if type(i) == dict:
    for k,v in i.items():
        l3.append(k)
        l3.append(v)

print(l3)

for i in l3:
  if type(i) == str:
    print(i)

#Question 13: Try to find alphanumeric in data
for i in l3:
  if type(i) == str:
    if i.isalnum() == True:
     print(i)

#Question 14: Multiplication of all numeric value in individual collection set
answer = 1
for x in l3:
  if type(x) == int:
    answer = answer * x

print(answer)

#Question 14: Multiplication of all numeric value in individual collection set

result_tuple = 1
result_set = 1
result_dict = 1
for i in l:
  if type(i) == tuple:
    for j in i:
      if type(j) == int:
        result_tuple = result_tuple * j
  if type(i) == set:
    for j in i:
      if type(j) == int:
        result_set = result_tuple * j
  if type(i) == dict:
    for k,v in i.items():
      if type(k) == int:
        result_dict = result_dict * k
      if type(v) == int:
        result_dict = result_dict * v

print(result_tuple,result_set,result_dict)


#Question 15: Unwraping all data into flat list
def flatten_list(list):
    flat_list = []
    # Iterate through the outer list
    for element in list:
        if type(element) == list or type(element) == set or type(element) == tuple or type(element) == dict:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))



