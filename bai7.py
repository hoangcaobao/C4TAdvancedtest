a=[1,5,-9,3]
print("Hi there,this is our sequence")
for i in range(len(a)):
    print(a[i])
themvao=int(input("What do you you want to add:"))
a.append(themvao)
b=[]
for i in range(len(a)):
    b.append(a[i])
a[0]=a[len(a)-1]
for i in range(1,len(a)):
    a[i]=b[i-1]

for i in range(len(a)):
    print(a[i])
