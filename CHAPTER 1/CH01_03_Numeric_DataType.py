#numeric
#int,float,complex

a="10"
b=100
c=14.05  
d=8+8j;   # real+imagenary

#printing the variables
print(a)
print(b)
print(c)
print(d)
print("    ")

#printing types of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("    ")

#print(type(a),type(b),type(c),type(d))

# Integer...
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
print("    ")

# Float...
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
print("    ")

# Complex...
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
print("    ")

# Type Casting...
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
print(a)
print(type(a))
print("    ")

#convert from float to int:
b = int(y)
print(b)
print(type(b))
print("    ")

#convert from int to complex:
c = complex(x)
print(c)
print(type(c))
print("    ")