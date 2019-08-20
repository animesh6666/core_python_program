f1=open("getdata.txt","w")
f= open("Student.txt","r")


n=int(input("Enter your class size : "))

student=[]

for i in range(n,n+n):
    name=input("Enter Student name: ")
    student.append(name)

    rn=int(input("Enter Student roll number: "))
    student.append(rn)
    
    ClassName=int(input("Enter Student Divison: "))
    student.append(ClassName)
    
i=f.read()   

for i in f:
    print(f1.write(i))

s = f.Student()
s.getdata(name,rn,ClassName)
s.setdata()


