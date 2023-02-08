t=("hello",10,False,43.2,"welcome",10,[15,25,42])
t2=tuple(("abc","xyz","pqr"))

print(t,type(t))
print(t2,type(t2))
print("     ")

Empty_tuple = ()
print(Empty_tuple)
print("     ")

# Count..number of repeated value
print(t.count(10))
print("     ")

# slicing
print(t[1:4])
print(t2[1])
print("     ")

# return Index of element...
print(t.index(10))
print("     ")

# Nested Tuple...
Nested_tuple = ("Mouse",(1,2,3),[3,2,1])
print(Nested_tuple)
print(Nested_tuple[1])
print("     ")

#to be able to change (convert tuple into list):
l=list(t2)
print(l,type(l))
l[1]="hey"
t2=tuple(l)
print(t2)
print("     ")

# to add items in tuple
l1=list(t2)
l1.append("coding")
t2=tuple(l1)
print(t2)
print("     ")

# remove from...
l1=list(t2)
l1.remove("coding")
t2=tuple(l1)
print(t2)
print("     ")

#unpacking a tuple
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)
print("     ")

#joining two tuple
t3=t+t2
print(t3)