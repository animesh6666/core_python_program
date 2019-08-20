import re

def re_split():
    print("Syntex \t\t:\tre.split(pattern,string,maxsplit)  ")
    print("String \t\t:\tmy name is animesh.")
    print("Pattern \t:\tr'\s'")
    print("Maxsplit \t:\t2")
    a = 'my name is animesh.'
    b=re.split(r'\s',a, maxsplit=2)
    print("Result \t:\t",b)

def re_match():
    print("Syntex \t\t:\tre.match(pattern,string)  ")
    print("String \t\t:\tmy name is animesh.")
    print("Pattern \t:\t'(m\w+)\W(n\w+)'")
    a = "my name is animesh."
    b = re.match('(m\w+)\W(n\w+)',a)
    print("Result \t:\t",b)

def re_search():
    print("Syntex \t\t:\tre.search(pattern,String)  ")
    print("""String \t\t:\tmy name is animesh.
                            am istudent""")
    print("Pattern \t:\t'a\w+'")
    a ='''my name is animesh.
        am istudent'''
    b = re.search('a\w+',a,re.MULTILINE)
    print("Result \t\t:\t",b)

def re_findall():
    print("Syntex \t\t:\tre.search(pattern,String)  ")
    print("""String \t\t:\tmy name is animesh.
                            am istudent""")
    print("Pattern \t:\t'a\w+'")
    a ='''my name is animesh.
        am istudent'''
    b = re.findall('a\w+',a)
    print("Result\t\t:\t",b)

def re_sub():
    print("Syntex \t\t:\tre.search(pattern,replace String,String)")
    print("""String \t\t:\tHello World""")
    print("Pattern \t:\t'World'")
    print("replace String \t:\t'India.'")
    a ='''Hello World'''
    b = re.sub('World','India.',a)
    print("Result\t\t:\t",b)

def re_compile():
    print("Syntex \t\t:\tre.search(pattern,flags)")
    print("""String \t\t:\tHello World""")
    print("flags \t\t:\tflags=re.I")
    a ='''Hello World'''
    c = re._compile(a,flags=re.I)
    print("Result\t\t:\t",c)
    b = re.sub('World','India.',a)
    print("Result of Sub\t:\t",b)

def re_escape():
    print("Syntex \t\t:\tre.search(String)")
    print("""String \t\t:\tHEllo @@ world.""")
    a ='''HEllo @@ world.'''
    b = re.escape(a)
    print("Result\t\t:\t",b)

def re_fullmatch():
    print("Syntex \t\t:\tre.search(compare String,String)")
    print("""compare String \t\t:\tHello""")
    print("String \t\t:\tHello World.")
    a ='''Hello'''
    b = "Hello World "
    b = re.fullmatch(a,b)
    print("Result\t\t:\t",b)

def re_finditer():
    print("Syntex \t\t:\tre.search(pattern,String)")
    print("""String \t\t:\tHello World""")
    print("pattern \t:\tr'\w'")
    a ='''Hello World'''
    b = re.finditer(r'\w',a)
    print("Result\t\t:\t",b)

def re_subn():
    print("Syntex \t\t:\tre.subn(pattern,String,string,intiger)")
    print("""String \t\t:\ta""")
    print("""String \t\t:\tb""")
    print("""intiger \t\t:\t3""")
    print("pattern \t:\thello world.")
    a='hello world.'
    b=re.subn(a,'a','b',3)
    print(b)

print("\t\t\t\tREGULAR EXPRESSION")
print("Functions of Regular Expression's Mathod  :  ")
print('')
print('''1.re.split()\n
        2.re.match()\n
        3.re.search()\n
        4.re.finalall()\n
        5.re.sub()\n
        6.re.compile()\n
        7.re.escape()\n
        8.re.fullmatch()\n
        9.re.finditer()\n
        10.re.subn()
        ''')

number =int(input("Enter your mathod number  :  "))

if(number==1):
    re_split()
elif(number==2):
    re_match()
elif(number==3):
    re_search()
elif(number==4):
    re_findall()  
elif(number==5):
    re_sub()   
elif(number==6):
    re_compile()
elif(number==7):
    re_escape()
elif(number==8):
    re_fullmatch()
elif(number==9):
    re_finditer()
elif(number==10):
    re_subn()
else:
    print("Please Enter valid number.")