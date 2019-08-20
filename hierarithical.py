class A:
    def __init__(self):
        print("MY name is Animesh. ")

    """def __del__(self):
        print("Program over.")"""

class B(A):
    def __init__(self):
        A.__init__(self)
        print("I am Student.")

class C(A):
    def __init__(self):
        super().__init__()
        print("I am 18 year old.")

class D(A):
    def __init(self):
        super().__init()
        print("I am Boy.")
    

b = B()
#print("   ",end=\n)
c = C()
#print("     ",end=\n)
d = D()
