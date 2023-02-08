#Python Lambda
#small anonymous function and  can take any number of arguments, but can only have one expression.
#********lambda arguments : expression**********


#Add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(5))



#Multiply argument a with argument b and return the result
x = lambda a, b : a * b
print(x(5, 6))



#Summarize argument a, b, and c and return the result
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



#Use that function definition to make a function that always doubles the number you send in
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))


#for triples the number u send
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))


#use the same function definition to make both functions, in the same program
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))




#************EXERCISE*************
#Create a lambda function that takes one parameter (a) and returns it.
x = lambda a : a
print(x)