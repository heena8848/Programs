class myclass:
    x=5
p1=myclass()
print(p1.x)


#The __init__() function
class Person:
    def __init__(self , name, age):
        self.name=name
        self.age=age
p1=Person("Heena",20)
print("Name is: ",p1.name)
print("age is: ",p1.age)


#The __str__() function
class Person:
    def __init__(self , name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=Person("Heena",20)
print(p1)


#Object methods
class Person:
    def __init__(self , name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is" + self.name)
p1=Person(" Heena",20)
p1.myfunc()


#The self parameter...use anything in place of self parameter
class Person:
    def __init__(xyz , name, age):
        xyz.name=name
        xyz.age=age
    def myfunc(abc):
        print("Hello my name is" + abc.name)
p1=Person(" Heena",20)
p1.myfunc()



# propties+action
# properties : variable (one word value)
# action : method process
class Dog:
    def __init__(me):
        me.name = "Tommy"
        me.breed = "Vodaphone wala kutta"
    
    def bark(x):
        print("my dog is barking... ",x.name,x.breed)

x = Dog()
x.bark()