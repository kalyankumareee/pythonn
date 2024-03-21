#--->while loop
#---->break using while loop

#eg:1
 #iterate from 20 to 30 and break the loop in 27
"""
#1)
i=20
while i<31:
    if i==27:
        print(i)
        break
    i=i+1
    
#2)    
i=20
while i<31:
    print(i)
    if i==27:
        break
    i=i+1

"""
#--->continue
"""
i=19
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)
"""
#while to iterate from 12 to 22 find the sum of all numbers
'''
1)
i=12
sum=0
while i<23:
    sum=sum+i
    print(sum)
    i+=1
   
#2)
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)

#eg:6    
#find the average of value from 20 to 25

i=1
sum=0
count=0
while i<5:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)


i=20
while i<=25:
    print(i)
    i+=1

#----->nested for loop
#eg:1
for row in range(1,3+1):
    for col in range(1,4+1):
        print(row,col)
          
#eg:2

for row in range(4):
    for col in range(4):
        print("*",end=" ")
    print()

sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum,end=" ")
    print()


# to print stars in right angled triangle

for row in range(0,5):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

row=6
col=6
for row in range(0,row):
    for col in range(0,col):
        print("*",end=" ")
    print()

for row in range(0,5):
    for col in range(0,5):
        if col==0 or col==5-1 or row==0 or row ==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

for row in range(5):
    for col in range(5):
         if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



for row in range(5):
    for col in range(5):
        if (col==0 or (col==1 and row==1) or (col==2 and row==2) or (col==3 and row==3) or (col==4 and row==4) or row==5-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#---->list


#--->data types
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary


#---->list?

1)if the collection of elements are surounded by square brackets, it is cosider
to be list
eg:
    L1=[4,7,9,9.86,"hello",7+91,[8,9,0]]

charactristics of list
1)list have to be surrounded by[]
2)it is mutable (the elements in the list are changable)
3)every elements inside list is indexed
4)the elements inside list will be ordered format
5)it can hold duplicate values
6)its heterogenous

#to access the elements in the list
L1=[1,4,1,7,89.7,7.5,"p","i"]
print(L1)

#--->Indexing
in the collection data types likes lidt,tuple,string,the elements will be alloted
with pre-defined unique value called index value

#we have 2 types of indexing
positive indexing--->starts with 0 from left hand side
negitive indexing--->starts with -1 from right hand side

# Positive indexing
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])

#negitive indexing
lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-4])
print(lst1[4])
print(lst1[0])

#slicing
lst1=[1,4,1,7,89.7,7.5,"p","i"]
#lst1[start_index:end_index:step]
print(lst1[0:4])
print(lst1[6:8])
print(lst1[:4])
print(lst1[4:])

print(lst1[0:7:1])
print(lst1[0:7:2])

#trail=int(input())

lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-4:-1])
print(lst1[-1:-4])
'''
#! To insert ot add element inside list
# append()-> used to add elelement at last position of list
L1=[9, 8, 0, 6]
L1.append ("car")
print(L1)



























































































































































































