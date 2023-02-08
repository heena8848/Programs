s={"apple","banana","cherry","apple",True,10,5.6}
s1=set(("apple",False,"cherry"))
print(s,type(s))
print(len(s))
print(s1,type(s1))
print(len(s1))

#check if apple is present in the set
print("apple" in s)

#add item in set
s1.add("banana")
print(s1)

#remove item from set
s1.remove("cherry")
print(s1)

#add element from s into s1
s1.update(s)
print(s1)

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Loop through the set, and print the values:
for x in s1:
  print(x)

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)