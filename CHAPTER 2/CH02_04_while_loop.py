i=1
while i<6:
    print(i)
    i+=1
        #or
i=1
n=5
while i<=n:
    print(i)
    i+=1

#calculate sum of numbers until the user enters zero
total=0
number=int(input("enter a number: "))
while number!=0:
    total=total+number
    number=int(input("enter a number:"))
print("total=",total)
    
