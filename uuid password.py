import uuid
import random

a = uuid.uuid4().hex
print(a)
password = str(a)

def delete(str,n):
    d = str[:n]+str[n+1:]
    return d

for i in range(6):
    
    b = random.choice(password)

c = list(b)
print(c)
random.SystemRandom().shuffle(c)
d = ''.join(c)

    #p = ''.join(c)
print(d)

    
#for j in range(32):
   # b = delete(password,j)
   # print(b)
