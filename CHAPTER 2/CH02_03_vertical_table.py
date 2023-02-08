a=int(input("enter starting number: "))
b=int(input("enter ending number: "))

for i in range(1,11):
    for j in range(a,b+1):
        #print(j,"*", i , "*", i*j,end=" | ")
        print(f"{j:2} * {i:2} = {i*j:2}",end=" | ")
    print()