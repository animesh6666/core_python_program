class A:
    def __init__(self):
        print("MY name is Animesh. ")

    def __del__(self):
        print("Program over.")

class B(A):
    def __init__(self):
        A.__init__(self)
        print("I am Student.")

class C(A):
    def __init__(self):
        super().__init__()
        print("I am 18 year old.")  

class D(B,C):
    def __init__(self):
        super().__init__()
        C.__init__(self)
        print("I am Boy.")

#a =A()
#b = B()
#print('\n')
#c = C ()
d = D()
