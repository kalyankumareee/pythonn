'''
#eg:3
def profile(name,age,place):
    txt="my name is {}.iam {} years old.iam from {}."
    print(txt.format(name,age,place))
profile("sid",29,"cbe")

#---->function with return statement
#return



1)a variable declared inside the function can be accessed outside the function
using return
2)return does not print anything
3)we cannot write any code below return statement

def f1():
    z=8
f1()
print(z)  #error--->cannot use outside the function


def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#123
def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a=input("enter the value:")
palindrome(a)
#based on the declaration of parameter and args
#functions are divided into 5 catagories

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args

#--->positional args
eg:1
def profile(phone,name,marks):
    txt="my name is {}.my phone number {}.i got {} marks."
    print(txt.format(phone,name,marks))
profile("sid",8963489754,78)


# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)

# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
profile("shashank",mark=98,phone=9876543210)
#default args
#the method of assigning the argument to the paremeter while declaring the
#function


Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

eg:2
# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)


# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="Usman", " Charan ", " NAresh "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("USman", 'Ussu', 'Alone')

'''

# Eg:2
'''
def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
print("My name is", val,"My age is",age)("kalyan",'name2','name3',28) # error ---> age has no args



def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
profile(28,"kalyan")
'''
#---> keyword variable length args
#---> are used to provide the args in the form of key value pair


#eg :1

'''
def price(price_list):
    print(price_list)
price(shirt=1000,iphone=80000)    
d1={"a":100,"b":200,"c":300}
d1=dict(a=100,b=200,c=300)
print(d1)
'''
'''
n = 5
{1:1,2:4,3:9,4:16,5:25}

n = int(input("Enter the number: "))
d1 = {}
for val in range(1,n+1):
    d1[val] = val**2
print(d1)


d1 = {"a":100,"b":200, "c":300}
d1 = dict(a=100,b=200,c=300)
print(d1)
'''

#object oriented programming
#The paradigms of objects oriented programming are

'''
class
objects
inheritance
polymarphism
abstraction
encapsulation

# Class is a blue print of an object
l1 = [1,2,3,4,5,6,]

# Eg:1
class c1:
    name1 = "Adi"
    print(name1)
   

# Eg:2
class person:
    name = "Adi"

c = person() # c as object
The process of creation an object
print(c.name)
'''
#eg-3
#create of a method
#when the function is created with a class is called as method
#method without parameter
'''
class person:
    def display():
        print("hello welcome to classes")

p=person()
p.display()
'''

#eg-4
#method with parameter
'''
class person:
    def display(person,name,age):
        print(name,age)
        
p=person()
p.display()
'''

# eg-5

'''
class person1:
    fname="siddu"
    lname="T"
    def first_name(person):
        print(person.fname)
    def full_name(person):
        print(person.fname+" "+person.lname)
    
p=person1()        
p.first_name()
p.full_name()
'''

#eg-6
#constructor---> int()
class profile:
    def __init__(self):   # constructor method
        print("hey")
p=profile()        # thought this process
















