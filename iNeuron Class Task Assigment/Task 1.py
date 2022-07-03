# KISHOR DEVARAGUDI iNEURON TASK 1:
s = "this is My First Python programming class and i am learNING python string and its function"

# Try to extract data from index one to index 300 with a jump 0f 3
# Try to reverse a string without using reverse function
# Try to split a string after conversion of entire string in uppercase
# Try to convert whole string into lower case
# Try to capitalize whole string
# Write difference between isalnum() and isalpha()
# Try to give an example of exapand tab
# Give an example of strip, lstrip and rstrip
# Replace a string character by another character by taking your own example
# Try to give a definition of string center function with an example
# Write your definition of compiler and interpretor without copy paste from internet
# Python is an interpreted or compile language. Give a clear answer with your understanding
# Try to write a use case of python with your understanding
# Try to extract data from index one to index 300 with a jump 0f 3

#1.Try to extract data from index one to index 300 with a jump 0f 3
S = "this is My First Python programming class and i am learNING python string and its function"
P = S[1:300:3]
print(P)

#2.Try to reverse a string without using reverse function
print(S[::-1])

#3.Try to split a string after conversion of entire string in uppercase
S1 = S.upper()
print(S1.split(' '))

#4.Try to convert whole string into lower case
print(S.lower())

#5.Try to capitalize whole string
print(S.capitalize())

#6.Write difference between isalnum() and isalpha()
print("""The Python isalpha() method returns true if a string only contains letters where as Python isalnum() only returns true if a string contains alphanumeric characters, without symbols""")
s2 = 'dsadw323'
print(s2.isalnum())
s1 = 'asdsasa'
print(s1.isalpha())

#7.Try to give an example of exapand tab
g = 'kishor\tDevragudi\tFrom\tHaveri'
print(g.expandtabs())

#8.Give an example of strip, lstrip and rstrip
t = "    ds   dsa  d sadas "  #Leading and Trailing space only stripped
print(t.strip())
'ds   dsa  d sadas'
print(t.lstrip())  #Only leading Spaces stripped
'ds   dsa  d sadas '
print(t.rstrip()) #Only Trailing Spaces stripped

#9.Replace a string character by another character by taking your own example
str = 'kishor.f'
str2 = str.replace('f', 'D')
print(str2)

#10.Try to give a definition of string center function with an example.String 'Center' function returns a centered string of length width.
g = 'kishor'
g.center(30,'#')


#11.Write your definition of compiler and interpretor without copy paste from internet
print('''In simple words, Compiler scans the program written and translates this into code that machine can understand whereas Interpreter takes one single line of code at a time. This basically means that compiler generates an intermediate machine code whereas interpreter doesn't.

Example of Programming Languages that use Compiler are C, C++, Java Example of Programming Languages that use Interpreter are JavaScript, Ruby

Python is an interpreted or compile language. Give a clear answer with your understanding
In various books of python programming, it is mentioned that python language is interpreted. But that is half correct the python program is first compiled and then interpreted. The compilation part is hidden from the programmer thus, many programmers believe that it is an interpreted language. The compilation part is done first when we execute our code and this will generate byte code and internally this byte code gets converted by the python virtual machine(p.v.m) according to the underlying platform(machine+operating system''')

#12.Try to write a use case of python with your understanding
print("""Some Use Cases of Python:

Data Science
Game Development
Web Applications
Software Development
Web Scraping
Internet of Things""")