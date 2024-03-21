#---->common function for list
'''
l1=[6,7,8,9,0]
print(len(l1))
print(min(l1))
print(max(l1))

l1=[6,8,9,"p","u"]
print(max(l1))  ---->erroe coz its a combination of int and string
print(min(l1))  ---->erroe coz its a combination of int and string

l1=[6,7,8,9,0,8.89,5,0.78]
print(max(l1))
#index()---->to get index value of specific element
print(l1.index(5))


#count()---->how many num of times an element is repeated
print(l1.count(6))

#some functions which is specifically used for list
#to add element inside list

# To add element inside list
#insert(indec_value,element)--> to add element at specific index position
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)

# pop(inde_valve) --> used to delete element at specific index

l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.pop(5)
print(l1)

# * remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1)

# * clear() --> to complete delete all element in list
l1.clear()
print(l1)


#...>join 2 list

l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)


#or
#extend()....>to combine 2 lists
l1.extend(l2)
print(l1)

# ? ---> copy()
# l1 = [6, 7, 8,9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

#diff between shallow copy and deep copy
#shallow copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)

#deep copy--->used to copy the list with nested list
import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])

l2=copy.deepcopy(l1)
l1.append("cars")
print(l1)
print(l2)

#sort---->arrange elements in list in ascending or descending order
l1=[9,7,45,0,-6,5,12]
l1.sort()#to arrange in ascending order
print(l1)

l1.sort(reverse=True) #to sort in descending order
print(l1)


l1=['z','d',9,'f','t','g']
l1.sort()
print(l1)#error

#list constructor
#list()---->to conver other collection datatype to list
l3=((8,9,3,6,7))
print(list(l3))

l4=(8,9)
print(list(l4))

#---->nested list
l1=[8,9,[0,8,7],["p","0",'y'],[8,'t']]
print(len(l1))
print(l1[-2])
print(l1[1:4])
print(l1[1:-1])

#to delete"t" from l1
l1=[8,9,[0,8,7],["p","0",'y'],[8,'t']]
l1[-1].remove('t')
print(l1)


#combine these ["p","0",'y'],[8,'t'] 

l1=["p","0",'y']
l2=[8,'t']
l3=(l1+l2)
print(l3)

#----->tuple
#characterstics of tuple
1)tuple have to be surrounded by()
2)the elements inside tuple are not changable
3)the elements inside tuple are indexed
4)the element will execute in order
5)it is heterogenous
6)it allow duplicate elements

eg:1
t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+3-6)
print(t1)
print(type(t1))#tuple

#indexing ,slicing are all same as list 

l1=[8]
print(type(l1))#list

l1=(8,)
print(type(l1))#tuple

l1=8,9
print(type(l1))#tuple

#len(),min(),max(),index(),count()--->all same as list

#to add element inside tuple--->cannot add
# cannot delete any element from tuple


# * jon 2 tuples

t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1 + t2)

# To add all element inside list and tuple
sum()
l1 = (8, 9, 7, 6)
#print(sum(l1))



# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)

# Iterate based on index value

l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])


#iterate based on index value
l1=[9,8,7,6,5,4,3,2]
for i in range(0,len(l1)):
    print(l1[i])
          
#----->strings
s1='0'
print(type(s1))

s1="0"
print(type(s1))

s1="hello world"
print(s1) #to access string

#indexing and slicing --->same as list and tuple

#len(),min(),max(),index(),count()
s1="hello world"
print(len(s1))
print(max(s1))
print(min(s1))

#ord()--->used to find the ASCII value of a character
s1='u'
print(ord(s1))

#strip()--->to eliminate the space in beginning and end of string
s1=" where are you"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

#split()--->to split the words in string based on a character
s1=" where are you?"
print(s1.split(" "))
print(s1.split("r"))

#replace()-->to replace a specific char in the string

s1="where are you?"
print(s1.replace('r','&&'))

#swap case()--->to convert captial to small and small to capital at a time
s1='HEY there'
print(s1.swapcase())

#title()---->to write the string in format of title
s1='never giveUP'
print(s1.title())
print(s1.capitalize())#--->1st char of string will be converted to capital

#join the string
s1="hello"
s2='world'
print(s1+s2)
'''

#s1='''how are you
#iam fine
#hey there

'''
print(s1.splitlines())#-->splitline used to split the string based on lines

#find() function
s1="hello world"
print(s1.index("r"))
print(s1.find('w'))

#join()
l1=["hey","there"]
print(" ".join(l1))
print("$".join(l1))

s1="wellcome to all"
print(s1.endswith('l'))
print(s1.startswith('w'))

s1="67"
print(type(s1))
print(s1.isdigit())

#print the string in reverse manner

s1="welcome to all"
print(s1[::-1])

#-->eg:1
#swap to find the number of lower case letters
s1="HEY THERE YOU aRE"
count=0
for i in s1:
    if i.islower():
        print(i)
        count+=1
print("the total num of lower case letters:",count)

s1='restarter'
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst,"$")
print(fst+txt)
'''

s1='''Lorem Ipsum is simply dummy text of the printing
and typesetting industry. Lorem Ipsum has been the
industry's standard dummy text ever since the 1500s
when an unknown printer took a galley of type and scrambled
it to make a type specimen book. It has survived not only
five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum.'''
char=len(s1)
print(char)
words=s1.split()
print(len(words))
sentenses=s1.split(".")
print(len(sentenses))
space=s1.split(" ")
print(len(space))
for val in sentenses:
    if val==" ":
        print(sentenses.index(" "))
        sentenses.pop(index)
print(len(sentenses))
space=0
for val in s1:
    if val==" ":
        space=space+1
print(space)












