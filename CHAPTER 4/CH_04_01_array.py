#Arrays same as list, but contains same data type
# Create an array containing car names
cars = ["Ford", "Volvo", "BMW"]
print(cars)


# Get value of first array
x=cars[0]
print(x)


# Modify first array
cars[0]="Toyota"
print(cars)


# Return length of array..
x=len(cars)
print(x)


# looping array elements
# print each items in the cars array
for x in cars:
    print(x)

# add element
cars.append("Honda")
print(cars)

# remove element
cars.pop(1)
print(cars)

#with remove()
cars.remove("Honda")
print(cars)