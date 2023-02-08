#Create and call function
def my_function():
  print("Hello world!")
my_function()


#--->Singal Arguments
def my_function(name):
  print(name + " Ahuja")
my_function("Bhavna")
my_function("Heena")
my_function("Sahil")

#--->Multiple Arguments
def my_function(x,y):
  print(num1, " + ", num2 , " = ", num1+num2)
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
my_function(num1,num2)


#Arbitary Argument....when number of arguments is unknown
def my_function(*kids):
  print("The youngest child is " + kids[2] + " Ahuja")
my_function("Bhavna","Heena","Sahil")


#Keyword Argument
def my_function(child3,child2,child1):
  print("The youngest child is " + child3 + "Ahuja")
my_function(child1="Bhavna", child2="Heena", child3="Sahil")


#Arbitary Keyword Argument....when number of KEYWORD arguments is unknown
def my_function(**kids):
  print("Elder child is " + kids["elder"] + " Ahuja")
my_function(elder="Bhavna",middle="Heena",younger="Sahil")


#Default parameter value
def my_function(country="India"):
  print("I am from " + country)
my_function("canada")
my_function("Brazil")
my_function()
my_function("India")
    
  
#Passing a list as an argument
def my_function(food):
  for i in food:
    print(i)
fruits=["Apple","Banana","Cherry"]
my_function(fruits)


#Return Values
def my_function(x):
  return 5*x
print(my_function(3))
print(my_function(4))
print(my_function(5))


#The pass Statement
def myfunction():
  pass


#Recursion...
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



#***********EXERCISE************
#Create a function named my_function
def my_function():
    print("Hello from a function")
my_function()