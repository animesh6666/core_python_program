import random
#import numpy
import uuid

a = ['a','b','c',12,3,4,6,7,9]


print(uuid.uuid4())

"""print(random.choices(a, k=4))

state = random.getstate()

print(random.choices(a, k=4))

print(random.setstate(state))"""

print(numpy.random.choice(a,size = 3, replace = True ))



"""print(random.seed(6))

print(random.triangular(10,20,1))

print(random.randrange(12,16,1))

b = 'animesh1234'

print(random.SystemRandom('animesh1234').random(3))"""
