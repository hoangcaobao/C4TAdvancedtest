import math
def quadro(a,b,c):
    delta=b**2-4*a*c;
    if(delta<0):
        print("PT KHONG CO NGHIEM THUC")
        hoithem=input("MUON TIM NGHIEM AO KHONG (YES/NO):")
        if(hoithem=="YES"):
           m=math.sqrt(-delta)
           s=str(m)+"i" 
           print("NGHIEM MOT LA:")
           print(str(-b/(2*a)) + "+" + s)
           print("NGHIEM HAI LA:")
           print(str(-b/(2*a))+"-"+s)
    if(delta==0):
        print("PT NGHIEM KEP:")
        print(-b/(2*a)) 
    if(delta>0):
        print("NGHIEM MOT LA:")
        print((-b+math.sqrt(delta))/(2*a))      
        print("NGHIEM HAI LA:")
        print((-b-math.sqrt(delta))/(2*a)) 
    
x=int(input("NHAP HE SO 1:"))
y=int(input("NHAP HE SO 2:"))
z=int(input("NHAP HE SO 3:"))
quadro(x,y,z)