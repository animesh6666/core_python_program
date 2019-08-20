print("Enter A ")
a=int(input())

print("Enter B")
b=int(input())

print("Enter C")
c=int(input())

print("Enter D")
d=int(input())

if(a<b or a<c or a<d):
    print(a," is Smallest number.")

    if(a<b and a>c and a>d):
        print(b," is Greatest number.")

    elif(a<b and a<c and a>d):
        print(d," is Smallest number.")

    elif(a>b and a<c and a>d):
        print(c," is Greatest number.")

    elif(a<b and a>c and a<d):
        print(c," is Smallest number.")

    elif(a>b and a>c and a<d):
        print(d," is Greatest number.")

    elif(a>b and a<c and a<d):
        print(b," is Smallest number.")

    elif(a>b and a>c and a>d):
        print(a," is greatest number.")

else:
    print("All are equal.")

    
    
