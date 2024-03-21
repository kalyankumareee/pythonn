#1.) Python program to capitalize the first and last character of each
# word in a string
# 2.) Input : 128 # Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
"""
s1=("hello world")
s2=s1[0].upper()
s3=s1[-1].upper()

print(s2+s1[1:len(s1)]+s3)

n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")


n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
    print("yes")
else:
    print("no")


l1=[1,2,3,4]
l2=[5,6,7,8]

l3=[]
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)


---->set

charctristics of set
1)set can b e created using {}
2)the elements inside set are not indexed
3)does not allow duplicate values
4)it unordered
5)heterogenous
6)multable or changable

#eg:1
s1={9,89,7.76,8+7J,(8,7,5),"truck",'e'}
print(s1)


s1="google"
freq=0
for i in s1:
    freq+=1
    print(s1.split())

#eg2
#s2={5,8,98,[9,0]}
#print(s2)--->error
#eg:3
#min(),max(),len()

#eg:4
#to add element inside set
s1={8,78,67,'u'}
s1.add(45)#--->add
print(s1)
#update
s1.update("hello world")
print(s1)


#to delete element inside set
s1={8,78,67,'u'}
#s1.pop()
#print(s1)--->it delete random element

#delete specifc element we use remove()&discard()&clear()

#remove()
s1.remove(8)
print(s1)

#discard()
s1.discard(8767)
print(s1)

#clear()
l1={}
print(type(l1))#-=--->datatype is dict

s1=set()#to create empty set
print(type(s1))


s1={8,9,4,"r"}
s1.clear()
print(s1)


del s1
print(s1)


#join the sets
s1={9,0,8}
s2={9.90,"card",'t',56}
s3=s1.union(s2)#---->union function used for to combine 2 sets
print(s3)


s1={4,5,6}
s2={7,8,5,6}
#print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s1))


#isdisjoit(),issubset(),issuperset()

s1={1,2,3,4,5}
s2={3,2,7,8,9}
for val in s1:
    if val in s2:
        str1="its joint set"
print("its joint set")

#---->dictionary
eg:1
d1={1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))

charactersticks of dicionary
1)have to be surrounded by{}
2)it have to be in the form of key,value pair
3)it is mutable
4)duplicate keys are not allowed,duplicate values are allowed
5)it is unindexed
6)it is ordered
7)key does not allow mutable datatypes,value allow mutable datatype


d1={1:100,2:200,3:300,-4:400}
#to access elements in dictionary
print(d1)
#or
#to access the values
print(d1[-4])#---->o/p is 100

#some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

#to find min,max based on values
print(min(d1.values()))
print(max(d1.values()))

#to replace a value in dictionary
d1={1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)

#to delete element from dictionary
d1={1:100,2:200,3:300,4:400}
#popitem()-->used to delete the last key value pair in dictionary
d1.pop(2)
print(d1)

#clear(),del

#join 2 dictionary
d1={1:100,2:200,3:300,4:400}
d2={"a":"apple","b":"ball","c":"cat"}
d1.update(d2)
print(d1)

#get()--->used to get value from a key
d1={1:100,2:200,3:300,4:400}
#print(d1[300])
print(d1.get(2))

#to print all the keys
print(d1.keys())
print(type(d1.keys()))

#to print all the values
print(d1.values())

#iterating dictionary
for val in d1:#to iterate keys alone
    print(val)

for val in d1.values():#to iterate values alone
    print(val)

#to get both key and values
for key,val in d1.items():
    print(key,val)

#problem:1

n=10
for i in range(0,5):
    n+=1
    print(i)
print(" ")


#s1=['Gfg','is','best','for','Geeks']
#print(s1.replace("G","e" and "e","G"))


n=int(input("enter num of times:"))
integer=[]
float_value=[]
string=[]
for i in range(n):
    value=eval(input("enter the value:"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("pls provide data in int,float,string")
print(integer)
print(float_value)
print(string)
    
#return a set of elements present in set a or b,but not both
#set1={10,20,30,40,50}
#set2={30,40,50,60,70}
#o/p-->{20,70,10,60}


set1={10,20,30,40,50}
set2={30,40,50,60,70}
set3={}
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set1:
    if val not in set2:
        set3.add(val)
print(set3)

#s1=['Gfg','is','best','for','Geeks']
#for i in s1:
 #   print(s1.("G" replace "e") and ("e" replace"G"))
 
"""  

l1=[1,2,3,4]
l2=["a","b","c","d"]
d1={}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)






