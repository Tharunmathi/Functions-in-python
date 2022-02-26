#//////////////////////////////////////"FUNCTIONS ","BUILT IN FUNCTIONS","FILE-HANDLING","MODULES","EXCEPTION -HANDLING",
# "ANONYMS FUNCTIONS","MAP","FILTER","REDUCE","MULTI THREADING"/////////////////////////////////////////////////////////

def hello_world():
    print("Hello world!")
hello_world()
# creating a function with return statement
def my_func():
    a = 10
    b = 20
    c = a + b
    return c
print("The sum is:", my_func())
# creating a function without  return statement
def my_func():
    a = 10
    b = 20
    c = a + b
print("The sum is:", my_func())
# the arguments by enter from the user
"""def sum(a,b) :
    return a+b
a = int(input("enter the value of a:"))
b = float(input("enter the value of b:"))
print(sum(a,b))"""
# call by reference with immutable objects like list
def my_func(list1):
    list1.append(20)
    list1.append(30)
    print("inside the function", list1)
list1=[10,40,50,60,70]
my_func(list1)
print("outside the function ", list1)
# call by reference with mutable objects like strings
def my_string(string1):
    string1 = string1+"How are u"
    print("inside the function   ", string1)
string1 = " IAM THARUN  "
my_string(string1)
print("outside the string ", string1)

# REQUIRED ARGUMENTS IN FUNCTIONS
"""def my_func(name):
    message = "HI "+ name
    return message
name=input("ENTER UR NAME:")
print(my_func(name))
def calculate(a,b):
    return a+b
calculate(10,20)
def simple_interest(p,t,r):
    return (p*t*r)/100
p = float(input("Enter the principle amount? "))
r = float(input("Enter the rate of interest? "))
t = float(input("Enter the time in years? "))
print("Simple Interest: ",simple_interest(p,r,t))"""

# DEFAULT ARGUMENTS IN FUNCTIONS
def printme(name,age=22):
    print("My name is",name,"and age is",age)
printme(name = "john")
def printme(name,age=22):
    print("My name is",name,"and age is",age)

printme(name = "john")
printme(name ="Tharun",age=20)
# VARIABLE-LENGTH ARGUMENTS
def printme(*names):
    print("type of passed argument is ",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)
printme("john","David","smith","nick")
# KEYWORDS ARGUMENTS
# function func is called with the name and message as the keyword arguments
def func(name, message):
    print("printing the message with", name, "and ", message)

    # name and message is copied with the values John and hello respectively
print(func(name= "John", message="hello"))
# The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case
def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))
def food(**kwargs):
    print(kwargs)
food(a="Apple")
food(fruits="Orange", Vagitables="Carrot")
def add_sum(a,b):
    c=a+b
    d=a-b
    return c,d
result1,result2=add_sum(5,6)
print(result1,result2)
def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x:",x)
a=10
print(id(a))
update(a)
print("a:",a)
def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(list))
    print("x",lst)
lst=[10,20,30]
print(id(lst))
update(lst)
print("lst ",lst)
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
        print(c)
sum(5,6,34,56)
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person("Tharun", age =19, city = "vijayawada", ph = 9392746638)
a=10
def something():
    a=15
    print("inside the function:",a)
something()
print("outside the function:",a)
a=10
def something():
    print("inside the function:",a)
something()
print("outside the function:",a)
a=10 # global variable
print(id(a))
def something():
    a = 15
    x = globals()['a']  # if u have more than one local variabals
    print(id(x))
    print("inside the function:", a)
    globals()['a'] = 19  # to change the local variable we use globals() functions.
something()
print("outside the function:", a)

# Declare a variable and initialize it
x = 101


# Global variable in function
def mainFunction():
    # printing a global variable
    global x
    print(x)
    # modifying a global variable
    x = 'Welcome To Javatpoint'
    print(x)


mainFunction()
print(x)
 # PASSING A LIST INTO A FUNCTION
def counts(lst):
         even = 0
         odd = 0

         for i in lst:
              if i%2==0:
                  even =even+1
              else:
                   odd+= 1
         return even,odd


lst = [23,24,56,77,44,39,20,49,55,66,75]
even , odd = counts(lst)
print("even :{} and odd:{}".format(even,odd))
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)
def fun1(name, age):
    print(name, age)
"""Possible correct function calls

1.Positional arguments: fun1('Emma', 23)
2.keyword arguments: fun1(name='Emma', age=23)
Or, The positional argument must not follow the keyword argument"""
fun1("Emma", age=23)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"BUILD IN FUNCTIONS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#  integer number
integer = -20
print('Absolute value of -20 is:', abs(integer))

#  floating number
floating = -20.83
print('Absolute value of -20.83 is:', abs(floating))
# all values true
k = [1, 3, 4, 6]
print(all(k))

# all values false
k = [0, False]
print(all(k))

# one false value
k = [1, 3, 7, 0]
print(all(k))

# one true value
k = [0, False, 5]
print(all(k))
x =  10
y =  bin(x)
print (y)
test1 = []
print(test1,'is',bool(test1))
test1 = [0]
print(test1,'is',bool(test1))
test1 = 0.0
print(test1,'is',bool(test1))
test1 = None
print(test1,'is',bool(test1))
test1 = True
print(test1,'is',bool(test1))
test1 = 'Easy string'
print(test1,'is',bool(test1))
# /////////////////////////////////////////////////////////////////////////////"FILE-HANDLING"//////////////////////////
"""# f=open(r"C:\\Users\THARUN\OneDrive\Desktop\text to handwriting.txt","r")
# print(f.read())
# print(f.readline())
b=open(r"C:\\Users\THARUN\OneDrive\Desktop\text to handwriting.txt","a") # append to the end of the file
b.write("HEY IAM THARUN say,cheers!")
b.close()
b=open(r"C:\\Users\THARUN\OneDrive\Desktop\text to handwriting.txt","r")
print(b.read())
b=open(r"C:\\Users\THARUN\OneDrive\Desktop\text to handwriting.txt","w") # overwrites any existing file
b.write("say hi to all my name is tharun and iam from vizag!")
b.close()
b=open(r"C:\\Users\THARUN\OneDrive\Desktop\text to handwriting.txt","r")
print(b.read())

#c=open('C:\\Users\THARUN\OneDrive\Desktop\myfile.txt', 'x') # create a new file
#c.write("THIS IS MY NEW FILE AND IAM WRITING IN NEW FILE!")
#c.close()
#c=open("myfile.txt","r")
#print(c.read())

import os
os.remove(r"C:\\Users\THARUN\OneDrive\Desktop\text to handwriting.txt")"""
# open the file.txt in append mode. Create a new file if no such file exists.
#fileptr=open(r"C:\Users\THARUN\OneDrive\Desktop\file2.txt","x")  #create a file -->empty file
#fileptr = open(r"C:\Users\THARUN\OneDrive\Desktop\file2.txt", "w")

# appending the content to the file
#fileptr.write('''''Python is the modern day language. It makes things so simple.
#It is the fastest-growing programing language''')

# closing the opened the file
# fileptr.close()
#fileptr=open(r"C:\Users\THARUN\OneDrive\Desktop\file2.txt","r")#reading file
# print(fileptr.read())
"""import os
os.remove(r"C:\\Users\THARUN\OneDrive\Desktop\file2.txt")"""
# import os
# os.rmdir(r"D:\SEM_1\tharun")
# ////////////////////////////////////////////"MODULES//////////////////////////////////////////////////////////////////
import math
a= math.factorial(4)
print(a)
# help(math)
import sys
print(sys.path) #prints the path of sys
"""import calc  # a module is created with calc.py
from calc import *  # it will import everything;
a=9
b=7
p= add(a,b)
q=sub(2,3)
print(q)
print(p)
import calc
a = calc.person1["age"]
print(a)"""
import platform

x = platform.system()
print(x)
import platform

x = dir(platform)
print(x)
# ////////////////////////////////////////////////////////////////////"EXCEPTION HANDLING"/////////////////////////////
"""a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
try:
     print("open resource")
     print(a/b)
     k=int(input("enter the number:"))
     print(k)
except ZeroDivisionError as e:
             print("it is caused by dividing with zero")
except ValueError as e:
    print("it is caused by entering value error")
except Exception as e :
      print("Hey we cannot divide the number by zero .",e)
finally:
    print("Hello!")
    print("resource closed")
try:
    print(x)
except :
  print("An exception occurred")
x = -1

if x < 0:
      raise Exception("Sorry, no numbers below zero")"""

# //////////////////////////////////////////////"ANONYMOUS FUNCTIONS-FILTER,MAP,REDUCE//////////////////////////////////
def is_even(n):
    if n%2==0:
        print("even")
        return n%2 ==0
    else:
        print("odd")
nums=[1,2,3,4,5,6,7,8,9]
evens= list(filter(is_even,nums))
print(evens)
nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda n:n%2 == 0,nums))
print(evens)
doubles=list(map(lambda a: a*2,evens))
print(doubles)
from functools import *
sums = reduce(lambda a,b: a+b,doubles)
print(sums)
def div(a,b):
    if a<b:
        a, b = b, a
    print(a/b)
div(2,4)
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div = smart_div(div)
div(2,4)

print("main says:"+__name__)
print("hello")
print("world")
from calc import ad
def fun1():
    ad()
    print("the result of fun1")
def fun2():
    print("the result of fun2")
def main():
    fun1()
    fun2()
main()
# ///////////////////////////////////////"MULTI THREADING"/////////////////////////////////////////////////////////////
from threading import *
from time import  sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
                  print("Hello")
                  sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
                  print("Hi")
                  sleep(1)
t1 = Hello()
sleep(0.2)
t2 = Hi()
t1.start()
t2.start()
t1.join()
t2.join()
print("bye")
