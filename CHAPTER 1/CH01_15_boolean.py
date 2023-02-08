#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b == a:
  print("b is equal to a")
else:
  print("b is not equal to a")


# Following Will Return True...
print(bool("fruits"))
print(bool(15.2))
print(bool(["apple", "cherry", "banana"]))


# Following Will Return False...
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))



# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")