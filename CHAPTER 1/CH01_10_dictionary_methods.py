d={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964,
    "colors" : ["red","green","blue"],
    "year" : 2201
}
print(d,type(d))

x=d["model"]
print(x)

#check if key is represented or not
if "model" in d:
    print("Yes, 'model' is one of the keys in the d dictionary")

#change last year & use for adding also
d.update({"year":2020})
print(d)
print("      ")

#pop last key,value pair
d.popitem()
print(d)
print("      ")



# use dict method to create dictionary...
d1=dict(name="john",age=22,country="norway")
print(d1,type(d1))
print("      ")

#length of dictionary
print(len(d1))

#return value of key..
x=d1.get("age")
print(x)
print(d1.get("age"))#another way
print("      ")

#return Keys only..
y=d1.keys()
print(y)
print("      ")

#return values only before change...
z=d1.values()
print(z)
print("      ") 

#change value nd return value with keys...
d1["country"]="india" 
i=d1.items()
print(i)
print("      ")

#adding items...
d1["color"]="white" 
print(d1)
print("      ")

#update value...
d1.update({"color":"black"})
print(d1)
print("      ")

#add item
d["colors"]=["red","green","blue"]
print(d)
print("      ")

#delete from dictionary
del d["colors"]
print(d)