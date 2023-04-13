# Variables,constants and literals
# asigning value to site_name variables

site_name="this is Python "
print(site_name)

# "this is Python" is assigned value to site_name variable then i printed out the assigned to site_name

# changing the value of a variable in pyton

sit_name="this is Python"
print(site_name)
site_name="this is great"
print(site_name)
# the value of site_name is changed from "this is Python " to "this is great"

# assigning multiple value to mu;ltiple variables

A, B, C =8,0.2,"Hello"

print(A) #prints 8
print(B)  #prints 0.2
print(B)  #prints Hello

name1= name2="Joyce","Mumbi"
print(name1) # prints Joyce
print(name2) #prints Mumbi

# lists in Python
#append()=>it is used to add new items

names=["joy","Mary","Joe","jojo","mash"]
names.append(('John'))
print(names)

#insert()it is used to  add items in a list ut here you have to spcify the index where it should be placed
names=["joy","Mary","Joe","jojo","mash"]
names.insert(4,"james")


print(names)

# To access items in a list//
# i can acces amn item using the item's index
#index (0)"joy",index (1)"mary",index (2)"joe",index(3)

names=["joy","Mary","Joe","jojo","mash"]
print(names[3])
 
#using negative indexing we can access items starting from the end of the array
names=["jane","john","jade"]
print(names[-3])

#changing the value of items in list

names =["joy","mumbi","joe","sam"]
names[0]="susan"
print(names)

# removing items in a list
# you can use remove().pop(),del()

names=["joy","mumbi","joe","sam"]
names.remove("joy")
print(names)

#pop() removes the last item in the list

names=["joy","mumbi","joe","sam"]
names.pop(2)
print(names)

# del()you have to specify the item's index

names=["joy","mumbi","joe","sam"]
del names[1]
print(names)

# how to empty a list and still have reference to it  without getting an erro
#using clear()


names=["joy","mumbi","joe","sam"]
names.clear()
print(names)

