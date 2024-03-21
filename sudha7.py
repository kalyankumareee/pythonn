'''
set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break

    if c==3:
        for val in set3:
            if val in set2 or val in set1:
               flag=1
               break
if flag==0:
    print("Disjoint")
else:
    print("joint")
           

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [list1[i] + list2[i]
for i in range(len(list1))]

print(result)
'''


'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []
i = 0
while i < len(list1):
    combined_string = list1[i] + list2[i]
    result.append(combined_string)
    i += 1
print(result)
'''




# functions
#def
# functions is a block of code which is used to perform a specific functionality
#function can be created using def keyword

# function has 3 parts
#function declaration
#function definiton
#function call


#eg:

'''
def greet():
    print("welcome user!")

greet()    
'''

#eg-2
#/ function with parameter

def greeting(name):
    print("welcome",name)

for val in range(1):
    username=input("Enter the name:")
    greeting(username)
