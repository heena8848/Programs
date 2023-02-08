# Empty List...
E_List = []
print("     ")

#create a list using []
a=[10,5,2,25,33]
print("list: ",a)
print("     ")

#acess using index
print("value of given index: ",a[3])
print("     ")

#change value using index
a[2]=50
print("after change list: ",a)
print("     ")

#create list with different data type
b=["Heena", 564, "c3", "CE", "GIT"]
print("diff datatype list: ",b)
print("     ")

c=[number*number for number in range(1,6)]
print("\nlist c: ",c)
print("     ")

#list slicing
print(a[0:2])
print(b[-2:])
print(a[1: :3])
print("     ")

print("\nMETHODS OF LIST")

# LIST METHODS....
# sort the list...
a.sort()       
print("\nsorted list a: ",a)
print("     ")

# reverse the string....
b.reverse()    
print("\nreverse list b: ",b)
print("     ")

# adds at the end of the list....
a.append(51)    
print("\nappend at end in list a : ",a)
print("     ")

# insert value at given index...
b.insert(2,"ahuja") 
print("\ninsert at the given index in list b: ",b)
print("     ")

# remove element at index 5...
a.pop(5)
print("\npop element of given index from list a: ",a)
print("     ")

# remove ahuja from list..
b.remove("ahuja")    
print("\nremove element from list b: ",b)
print("     ")

d=[5,4,3,2,1]
# return index of given value..
x=d.index(2)
print("\nreturn index of given value: ",x)

# Extend elments of other list...
d.extend(a)
print("\nadd elememts of other list, at the end: ",d)

#copy of list...
d.copy()
print("\nreturns copy of the list: ",d)


# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# Print List items With Index NUmber...
for i,item in enumerate(thislist,1):
    print(i,item)


# containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
print(fruits)


# Syntax For List Comprehension...
# newlist = [expression for item in iterable if condition == True]
# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Print Number That Is Greater Than 5...
l = [x for x in range(11) if x >5]
print(l)


# Sort the list alphabetically....
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Sort the list descending...
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# Reverse the order of the list items...
thislist = [12,3,6,23,56]
thislist.reverse()
print(thislist)


# Join two list....
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


# Case sensitive sorting can give an unexpected result...
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)


# Clear the list content.....
print(thislist)
thislist.clear()
print(thislist)

