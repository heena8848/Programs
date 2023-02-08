#--->Open a file, read on the server
f=open("C:\\Users\workgroup\Desktop\CEC assessment.txt","r")
print(f.read())
print("-----------")
f=open("C:\\Users\workgroup\Desktop\CEC assessment.txt","r")
print(f.read(5))
print("----------")
f=open("C:\\Users\workgroup\Desktop\CEC assessment.txt","r")
print(f.readline())
f.close()

#WRITE to an existing file
f=open("CEC assessment.txt", "a")
f.write("include other functionality!")
f.close()
f=open("CEC assessment.txt", "r")
print(f.read())