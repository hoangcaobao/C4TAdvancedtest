a=[1,5,-9,3]
print("Hi there,this is our sequence")
for i in range(len(a)):
    print(a[i])
themvao=int(input("What do you you want to add:"))
# a[len(a)]=themvao
a.append(themvao)
for i in range(len(a)):
    print(a[i])