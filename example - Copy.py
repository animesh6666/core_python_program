a=int(input("Enter A =  "))
b=int(input("Enter B = "))
c=int(input("Enter C = "))
d=int(input("Enter D = "))

if(a>b):
    if(a>c):
        if(a>d):
            print(a," is Greatest number.")
        else:
            print(d," is Greatest number.")
    else:
        if(a<d):
            print(b," is Smallest number.")
        else:
            print(c," is Smallest number.")
else:
    if(a<c):
        if(a<d):
            print(a," is Smallest number.")
        else:
            print(d," is Smallest number.")
    else:
        if(a>d):
            print(b, " is Greatest number.")
        else:
            print(c," is Greatest number.")
            
        
            
        
                
           
        
