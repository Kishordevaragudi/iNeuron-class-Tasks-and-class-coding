# Draw triangle
n = int(input('Enter number of rows : '))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# Outer loop
# Draw ABCD triangle using while loop
n = 7
i = 1
while(i<=n):
  k = i
  j = 1
  while(j<=i):
    if chr(64+k) != "[" :
      print(chr(64+k),end = " ")
      k = k + n - j
      j = j + 1
  print("\r")
  i = i + 1

#try to print all the number divisiable by 3 in range(40-400)
for i in range(40,400+1):
    if i%3==0:
      print(i)



str = '''Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.
Python consistently ranks as one of the most popular programming languages.'''

def without_vowel(c):
    new_string = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    a = 0
    while a<=len(str)-1:
      if str[a].lower() in vowels:
        new_string = new_string.replace(str[a],"")
      a = a + 1
    return new_string

#Function Call
without_vowel(str)

for i in range(0,1000+1):  #Both included
    if i%2==0:
      print(i)

#define a function for all above problems:
def pattern1(n):
    i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1

pattern1(9)

def divby3(a,b):
  for i in range(a,b+1):
    if i%3==0:
      print(i)

divby3(40,400)

def divby2(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

print(divby2(0,1000))

