'kishor devaragudi'
# q1 : Try to print a prime number in between 1 to 1000
# q2 : Try to write a function which  is equivalent  to print function in python
# q3 : Try to write a function which is a replica of list append , extend and pop function
# q4 : Try to write a lambda function which can return a concatination of all the string that we will pass
# q5 : Try to write a lambda function which can return list of square of all the data between 1-100
# q6 : Try to write a 10 Different different example of lambda function with a choice of your taks
# q7 : Try to wwrite a funtion whihc can perform a read operation from .txt file

# Q1: Try to print a prime number in between 1 to 1000
for number in range(1, 1001):
   # all prime numbers are greater than 1
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)

# Q2 : Try to write a function which is equivalent to print function in python
import sys
def my_print(content):
  sys.stdout.write(content)

my_print("kishor")

# Q3 : Try to write a function which is a replica of list append , extend and pop function

#Replica of Extend


def my_extend(list,n):
  for x in n:
    j=len(list)
    list.insert(j,x)
  return list

my_extend([4,6,7],eval(input("enter list for extend")))

#Replica of Pop (Removes last index)

def my_pop(list1):
  list1.remove(list1[len(list1)-1])
  return list1

my_pop([4,5,6,100,86])

# Q4 : Try to write a lambda function which can return a concatenation of all the string that we will pass
#Approach 1
from functools import reduce
lst = ['abc','rtg','types']
reduce(lambda x,y: x+y,lst)

#Approach 2 (Better Approach)
args=('abc',77,'xyz',1,2,3)
print(''.join(list(filter(lambda x:type(x)==str,args))))


# Q5 : Try to write a lambda function which can return list of square of all the data between 1-100
lst = list(range(1, 101))
print(list(map(lambda x:x*x, lst)))

# Q6 : Try to write a 10 Different different example of lambda function with a choice of your task
#1. Doubling
double = lambda x: x * 2
print(double(5))

#2. Squaring in a given range
lst = list(range(1, 11))
print(list(map(lambda x:x*x, lst)))

#3. Concatenation of all string
args=('abc',77,'xyz',1,2,3)
print(''.join(list(filter(lambda x:type(x)==str,args))))

#4. Product of all elements in a list
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)

#5. Lambda with if-else
max = lambda a, b : a if(a > b) else b
print(max(100, 20))

# 6. Sorting a list and getting second largest element
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)

#7. Odd Numbers from the list
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

#8. Upper Case
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)

#9. Lower Case
animals = ['DOG', 'CAT', 'PARROT', 'RABBIT']
lowered_animals = list(map(lambda animal: str.lower(animal), animals))

print(lowered_animals)

#10. Cubing
lst = list(range(1, 11))
print(list(map(lambda x:x*x*x, lst)))

# Q7 : Try to wwrite a funtion which can perform a read operation from .txt file
def read(filename):
  f = open(filename,"r")
  if f.mode == "r":
    contents = f.read()
    print(contents)

read("Task 1.py")
