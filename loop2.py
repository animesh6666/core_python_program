i=1
while i<=5:
    j=5
    while j>i:
        print(" ", end =" ")
        j-=1
    m=1
    while m<=i:
        print(m , end = " ")
        m+=1
    print(" ")
    i+=1


print("\n for loop\n")

for i in range(1,6):
    for j in range(5,i,-1):
        print(" " , end =" ")
    for m in range(1,i+1):
        print(m, end = " ")
    print(" ")
    
    
