# take a value of length and breadth of a user and check if it is square or not

#l=int(input("enter the length value: "))
#b=int(input("enter the breadth value: "))
#if l  == b :
    #print("it is a square")
#else:
    #print("it is not a square")

#Eg:

# #program  to check whether the given integer is a multiple of 5 and 7


#n=int(input("enter the integer value: "))
#if n%5==0 and n%7==0:
    # print("yes")
#else:
   # print("no")


#Eg: write a program to accept the price of the bike and display the road tax to be paid
   #according to the following criteria :
   
   #Cost price(in Rs)                   Tax
  #>100000                              15 % + discount 6%
  #>50000 and <=100000                  10%
  #<=50000                              5%

   
#price=int(input("enter the cost of the bike: "))
#amount=0
#if price>= 100000:
   # discount=price*(6/100)
  #  value=price-discount
  #  amount=value*(15/100)
 #   print(value+amount)

#else:
    #tax=price*(5/100)
    #total=price+tax
    #print("the order cost of the bike is: ",total)



# if elif programs:
'''
# Eg:1
a=7
b=9
c=3
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater ")
else:
    print("c is greater")
    

#eg:4---> accept the age of 4 people and display oldest one
a=int(input("enter the marks: "))
b=int(input("enter the marks: "))
c=int(input("enter the age3: "))
d=int(input("enter the age4: "))
if a>b and a>c and a>d:
    print("a is greater")
elif b>a and b>c and b>d:
     print("b is greater")
elif c>a and c>b and c>d:
         print("c is greater")
else:
     print("d is greater")

'''
#a school has following rules for grading system:
"""
a=int(input("enter the marks:"))
if a>=80 and a<=100:
    print("grade A")
elif a>=60 and a<=80:
    print("grade B")
elif a>=50 and a<=60:
    print("grade C")
elif a>=40 and a<=50:
    print("grade D")
elif a>=30 and a<=40:
    print("grade E")
"""
#....>short hand if else
eg:1
a=9
b=8
'''
if a>b:
    print("a greater")
else:
    print("b greater")
'''
#print("A") if a>b else print("B")



'''
#rules
    1)statement inside the if condition have to be present at first
    2)elif cannot be used in short hand if else
    3)always it have to end with else 

'''
'''
#code to check the given char is vowel or consonent
char=input("enter the char:")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("vowel")
else:
    print("consonent")

#or

str1="aeiouAEIOU"
char=input("enter the char:")
if char in str1:
    print("vowel")
else:
    print("consonent")

#short hand if else

str1="aeiouAEIOU"
char=input("enter the char:")
print("vowels") if char in str1 else print("consonent")
'''
#...>elif ladder using short hand if else
#eg:1
#find greatest among 3 variables using shorthand if else
"""
a=8
b=5
c=9
print("A greater")if a>b and a>c else print("B greater")if b>a and b>c else print("c greater")

a=11//2
print(a)

x=4
X=x/2
print(X)

print("AB\nC\nDE")

"hello Mike".find("Mike")
"""
'''
#.....>looping
looping can be implimented using
for loop
while loop

#for loop
for loop is used for itearation,if we know the number of times the loop have to run
it is used to iterate the iterables eg(string,list,tuple,etc...)
'''
"""
for syntax in c:

for(i=0;i<10;i++){
    print("hello");
    }

#for syntax in python
for userdefined variable in range(start,end,step):default step value is 1
  statement
  statement
  statement
eg:1
"""
'''
#to print the value from 1to10 using loop
for i in range(0,10):
    print(i)

#eg:2
for val in range(23,50,2):
    print(val)

#eg:3
#to decrement value
'''
#for val in range(10,0,-1):
 #   print(val)

#eg:4
   # print the output of 7th multiplicaton table from 21 to 43
#method:1
#for val in range(1,10+1):
    #print('7','*',val,'=',val*7)

#method:2
'''
for val in range(1,10+1):
    #ans="7*{}={}"
    #print(ans.format(val,val*7))
    print("7*{val}={val*7}")

#eg:5
#break---->used to terminate the loop
'''
'''
for val in range(1,15):
    if val==5:
        break
    print(val)
''' 
'''
for val in range(5,100,5):
    
    if val==30:
        print(val)
        break
 #continue
    #eg:1
for val in range(1,10):
    if val==6:
        continue
    print(val)
'''
#practise problems
    #print the even numbers between 20 to 40
"""
for i in range(20,41):
    if i %2==0:
        print(i)
"""
#---->while loop
#while is used when we do not known the number of times loop have to run
#to iterate the non iterable elements while loop is used

#eg:1
#to iterate number from 1to 10
"""
i=0
while i<11:
    print(i)
    i=i+1
"""
'''  
for loop practise
write a program to display sum of odd numbers and even numbers that fall
between 12 and 37

# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
'''
'''
for i in range(12,37,2):
    for j in range(12,38,3):
        a=i+j
        print(a)
'''       
i=10
while i>0:
    print(i)
    i=i-1

#1st answer
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"

#2nd answer
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

#3rd answer
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

# 4th answer
n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)

#5th ansewer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)


























































































































































































