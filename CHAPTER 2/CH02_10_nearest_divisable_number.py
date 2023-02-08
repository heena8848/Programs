a=int(input("enter value: "))
b=int(input("enter value: "))

if b%a == 0:
    print("well done")
else:
    rem=b%a
    ans=b-rem
    ans2=ans+a
    print(ans,ans2)

math=input("choice:- floor or ceil value?  ")
if math=="floor":
    print(ans)
else:   
    print(ans2)     
