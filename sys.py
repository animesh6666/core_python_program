import sys
A = []
b=sys.argv
print(b)

for i in range(3):
        A.append([0]*3)

for i in range(len(A)):
        for j in range(len(A[0])):
                for m in range(1,10):
                        A[i][j]=b.append(m)

for i in range(len(A)):
        for j in range(len(A[0])):
                for m in range(1,10):
                        print(A[i][j],end = ' ')
                 #       A[i][j]=b.append(m)
