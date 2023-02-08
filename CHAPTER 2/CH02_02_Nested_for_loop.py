#inner loop will be executed one time for each iteration of the outer look:
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
    else:
        print("--------")


#EX(1):- one single table
for i in range(2,3):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
        print()


#EX(2):- multiple table
a=int(input("enter starting number: "))
b=int(input("enter ending number: "))

for i in range(a,b+1):
    for j in range(1,11):
        print("%2d * %2d = %2d"%(i,j,i*j))
        

