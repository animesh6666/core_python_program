class Student:
    __Class = 0
    __name = None
    __rn = 0

    def __init__(self,ClassName,name,rn):
        self.Class=ClassName
        self.name=name
        self.rn=rn

    def getdata(self):
        print(self.Class , end = '\t\t')
        print(self.name, end = '\t\t')
        print(self.rn, end = '\t\t')

n=int(input("Enter your class size : "))

st=list()

for i in range(n):
    name=input("Enter Student name: ")

    rn=int(input("Enter Student roll number: "))

    ClassName=int(input("Enter Student Divison: "))

    st.append(Student(ClassName,rn,name))

print('*******************************************************')  
print('\t\tDetails of Students ')
print('Divison\t\troll_number\t\tname')
for i in range(n):
    st[i].getdata()
    print('\n')