i =0
while i<5:
    j=0
    while j<i+1:
            print("*" , end = " ")
            j+=1
    print(" ")
    i+=1
    

print(" for loop")


for i in range(1,6):
    for j in range(1,i+1):
        print("*" , end = " ")
    print(" ")
