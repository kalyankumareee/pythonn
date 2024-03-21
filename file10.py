# ---> Tasks
'''
# Write the code for the below tasks using function

1) d1 = {"shirt": 1000,"pant": 1500,"Shoes": "900","handkey":30}
a) Find the min ans max priced product
b) Find the product start with 's' and 'S'5



# Polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1) Method overloading ---> It is not possible in python.
# 2) Method overriding.


# Method riding
# Polymorphism in classes


class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i=IOB()
i.ratio()


s=SBI()
s.ratio()



# Eg:2

class USA:
    def language(self):
        print("English")

    def capital(self):
        print("Washinton DC")

class India(USA):
    def language(self):
        print("None")

    def capital(self):
        print("New Delhi")

I = India()
I.language()
I.capital()



# Eg:3
# Polymorphism using objects

# c1, c2 --> c1 = print(c1),print(c2)
# f1, f2

class c1:
    def f1(self):
        print("class 1")

        
class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

#obj1=c2()
#obj1.f1()

obj2=c1()
obj2.f1()



def display(a):
    a.f1()
display(obj1)
display(obj2)

# Changing the functionality of builtin functions
class shopping:
    def __init__(self,l1):
        self.items=l1
    def __len__(self):
        length=len(self.items)
        return length

s=shopping([1,2,3,4,5])
print(len(s))

#eg:2
class summing:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2,6,10)
obj.add(3,4)
obj.add(1,2,3)


# Abstraction Method

class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

   def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
        
tr triangle()
tr.traingle_sides()
tr.name() 


# Rules to define abstract class 1

1) Abstract class cannot be instantiated.
2) From abc import ABC, abstract method.
3) Subclass the normal class with ABC.
4) Convert the normal method inside the abstract class to abstract method.
5) All the child classes have to be subclassed with abstract class.
6) The abstract method should be present in the child classes.



# Eg:2

# super() ---> used to access the parent class method from child class method.  
class c1:
    def m1(self):
        print("This is abstract class")

class c2:
    def m2(self):
        print("Iam child 1")

    def m1(self):
        pass

class2=c2()
class2.m2()


# Eg:3

# From abc import ABC, abstractmethod

class password:
    pswd="sidd1994$"


class login(password)
    def validate(self,name,password):
        if super().pwd()==password:
            print("Welcome",name,'!!')
            print("Login Sucessfull")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name=input("Enter the name: ")
pwd=input("Enter the password: ")
Login.validate(name,pwd)


# Encapsulation
# Eg:1

class car:
    __name="BMW"  # Private variable
    print(__name)

c1=car()
#print(c1.name) 
#c1.name="Audi"
#print(c1.name)



# ----> Eg:2
# Accessing private date outside the class

class c1:
    __phone="9704546461"

    def display(self):
        print(self.__phone)
c=c1()
c.display()


'''

# ---> Eg:3

# Declare private method

class class1:
    def __m1(self):
        print("Iam private method")

    def __int__(self):
        self.__m1()
c=class1()

 









































