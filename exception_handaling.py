a = print(input("ENter  A: "))
b = print(input("Enter B: "))

try:
    c = a/b
    raise ZeroDivisionError
    
except TypeError :
    print("This is wrong syntex.")
else :
    print(c)

finally:
    print("Your code is working.")
