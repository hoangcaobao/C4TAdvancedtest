a=[1,5,-9,3]
for i in range(len(a)):
    print(a[i])
menhlenh=input("Where do you want to delete (head/tail):")

if(menhlenh=="head"):
    a.remove(a[0])
if(menhlenh=="tail"):
    a.remove(a[len(a)-1])

for i in range(len(a)):
    print(a[i])
