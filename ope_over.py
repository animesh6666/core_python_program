class A :

    n1 = 0
    n2 = 0

    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2

    def __add__(self, other):
        temp = A(self.n1, self.n2)
        temp.n1 = self.n1 - other.n1
        temp.n2 = self.n2 - other.n2
        return temp

    def __sub__(self,sa):
        temp = A(self.n1,self.n2)
        temp.n1 = self.n1 % sa.n1
        temp.n2 = self.n2 % sa.n2
        return temp

    def __le__(self,other):
        temp = A(self.n1,self.n2)
        temp.n1 = self.n1 <= other.n1
        temp.n1  = self.n1 <= other.n1
        return temp

    
s1 = A(50, 40)
s2 = A(30, 90)
s3=s1+s2
print(s3.n1)
print(s3.n2)

s3 = s1 - s2
print(dir(s1))


print(s3.n1)
print(s3.n2)

print("less or equal.")
s3 = s1 <= s2
print(s3.n1)
print(s3.n2)
