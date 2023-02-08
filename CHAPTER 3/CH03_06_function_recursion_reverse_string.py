def rev(x):
    if(len(x)==0):
        return
    print(x[-1],end=" ")
    m=""
    for i in range(len(x)-1):
        m+=x[i]
    rev(m)
x=input("enter string: ")
rev(x)