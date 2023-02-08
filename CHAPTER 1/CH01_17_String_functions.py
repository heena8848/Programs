str="python is a high-level, general-purpose programming language.\npython is dynamically typed and garbage-collected.\nit supports multiple programming paradigms,including structured,object-oriented and functional programming.\n"
print(str)

#string functions
string="hello, world!"

#length of string
print("\nlength of string is: ",len(string))

#endswith
print("\nstring end with languag?: ",string.endswith("language"))

#count character in string
print("\ncounting h character in string: ",string.count("l"))

#capitalize string
print("\nstring capitalize: ",string.capitalize())

#find character/word in string
print("\nfind index of [world] in string: ",string.find("world"))

#replace string
print("\nreplace string: ",string.replace("hello","helloo"))
print("   ")

# Slicing...
print(string[:5])
print(string[2:])
print(string[-5:-2])


# Upper Case...
print("UPPER CASE: ",string.upper())

# Lower Case...
print("lower case: ",string.lower())

# Remove Whitespace...
a = "   Hello, World! "
print("remove space: ",a.strip())

# Split String...
a = "Hello World Wide"
print(a.split())


# String Concatenation...
a = "Hello"
b = "World"
c = a + b
d = a + " " + b # To Add Space Between Them...
print(c)
print(d)