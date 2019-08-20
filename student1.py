class Student:
    ClassName=3
    __i=0  
    __Class = 0
    __name = None
    __rn = 0
    
    def __init__(self,i):
        self.i=i
        #print(self.i)
        
    def setdata(self,ClassName,name,rn):
        self.Class=ClassName
        self.name=name
        self.rn=rn

    def getdata(self):
        print(self.Class, self.name, self.rn)


class sample (Student):
    ClassName=0
    name=None
    rn=0
    i=0

    def __init__(self,ClassName,name,rn,i):
        self.ClassName=ClassName
        self.name=name
        self.rn=rn
        #self.i=i

    Student.__init__(i)
    super().setdata(ClassName,name,rn)
    super().getdata()
    


n=int(input("Enter your class size : "))

student=[]

for i in range(n,n+n):
    
    name=input("Enter Student name: ")
    student.append(name)

    rn=int(input("Enter Student roll number: "))
    student.append(rn)
    
    ClassName=int(input("Enter Student Divison: "))
    student.append(ClassName)

    s=sample(name,rn,ClassName,i)

