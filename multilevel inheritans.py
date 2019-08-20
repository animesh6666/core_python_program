 class A:
    a=0
    b=0
    def A(self):
        print("Enter A : ")
        a=input()
        self.a=a

class B(A):
    def B(self):
        super().A()
        super().b
        print("Enter B : ")
        self.b=b
        b=input()

class C(B):
    
    def C(self):
        super().B()
        print(self.a)
        print(self.b)
        #c=a+b
        #print(c)
        
c1 = C()
c1.C()    

