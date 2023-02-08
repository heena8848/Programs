#Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Heena", "Ahuja")
x.printname()



#Child Class
class Student(Person):
  pass

x = Student("Heena", "Ahuja")
x.printname()


#Add the __init()__ method....
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self,fname, lname)

x = Student("Heena", "Ahuja")
x.printname()


#use super() function...
#you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Heena", "Ahuja")
x.printname()


#add properties
class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year  

x = Student("Heena", "Ahuja", 2020)
print(x.graduationyear)


#add methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()