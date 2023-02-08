#4 TYPES:----
# Formatting with % operator....
name="john"
age=23
print( "%s is %d years old." %(name,age))

mylist=[1,2,3,"hello"]
print("A list: %s" %mylist)

#---->Merge String.
data=("john","doe",53.44)
format_string="Hello %s %s. your current balance is $%s."
print(format_string % data)



# Formatting with string literals,called f-strings.....
print(f"{name} is {age} years old")

data=("john","doe",53.44)
print(f"hello {data[0]} {data[1]}. your current balance is $ {data[2]}")



# Formatting with format() string method....
price=49
txt="the price is {} dollars"
print(txt.format(price))
print("           ")

price=49
txt="the price is {:.3f} dollars"
print(txt.format(price))
print("           ")

quantity=5
itemno=564
price=49
myorder="i want {} peices of item number {} for {:.2f} dollars. "
print(myorder.format(quantity,itemno,price))
print("           ")

#---->using index number
age=36
name="john"
txt="His name is {1}. {1} is {0} years old."
print(txt.format(age,name))
print("           ")

#---->Named index
txt="His name is {name}. {name} is {age} years old."
print(txt.format(name="john",age=36))
print("           ")