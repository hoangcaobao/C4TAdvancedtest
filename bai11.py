def timsobenhat(a):
    benhat=a[0]
    for i in range(1,len(a)):
        if(benhat>a[i]):
            benhat=a[i]
    print(benhat)

def tinhgiaithua(b):
    tich=1;
    for i in range(1,b+1):
        tich=tich*i

def Fibonaci(n):
    a=[0,1]
    for i in range(2,n):
        a.append(a[i-1]+a[i-2])
    print(a[len(a)-1])

def phantich(a):
    b=[]
    for i in range(1,a+1):
        if(a%i==0):
            b.append(i)
    return b

def kiemtragiongnhau(a,b):
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i]==b[j]):
                c.append(a[i])
    return c

def Euclid(a,b):
    day1=phantich(a)
    day2=phantich(b)
    c=kiemtragiongnhau(day1,day2)
    print(c[len(c)-1])

Euclid(6,12)

def daochieuday(a):
    
    if (len(a)%2==0):
        c=int(len(a)/2)
        for i in range(c):
            x=a[i];
            a[i]=a[len(a)-1-i];
            a[len(a)-1-i]=x;
    
    else:
        c=int((len(a)-1)/2)
        for i in range(c):
            x=a[i];
            a[i]=a[len(a)-1-i];
            a[len(a)-1-i]=x;
    return a  
      




