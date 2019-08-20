#print function use for return value
print()

#input is use for given value by user.
input()

#int is store intiger value.
int()

#float is store intiger and float value.
float()

#bool is give true or false.
bool()

#complex is use for store complex structer.
complex()

#str use for making string.
str()

#list use for making list.
list()

#tuple is use for making tuple.
tuple()

#dict use for store pair.
dict()

#set is use for making set.
set()

#bin is used for converting in binry.
bin()

#oct is used for transform int value in octal.
oct()

#hex function converts value in hexadntional.
hex()

#chr used for finding char of given value.
chr()

#ord used for give ordinal value of given keyword.
ord()

#len function help for finding length.
len()

#sorted use for arrange  dectionary, set in order and it done in three ways .
#first it diractly arrange in diseding order.
#second if the reverse is true then it arrange in assding order
#third is arrange it by length.
a=['as',2,'d']
def t(d=2):
    return d
sorted(a)
sorted(a,reverse=True)
sorted(a,key=t)

#abs is transform nagative (absoult) value in intiger value and transform complex value in simple number.
abs(-23)
abs(23+2j)

#if all values of given iterable(set,dict,tumple,list) are same format then gives true.Empty iterable is false.
all()

#if all values of given iterable(set,dict,tumple,list) are same or some diffrent format then gives true.Empty or all iterable are diffrent then,false.
any()

#some printable characters like($,#) change in ascii and give their ascii value.
ascii()

#converts in boolian only,none, false, emply,0.0 are False.
bool()

                                                                        """"************"""
bytearray()


                                                                                        """ ****************"""
bytes()

#if functin is callable than it gives true.
callable()

                                                                                        """******************"""
classmethod()

#compile string in program.
#For first give name of source than ,file name and exec(codeobject)
compile(source,'filename','exec')

#delattr use for deliting object of class.
delattr()

#dir use for return the value of object if , it is empty than, return valid attributes.
dir()

                                                                                                    """************"""
divmod()

#object of list and tuples , this function gives number of this function;s object.
enumerate()

#eval is use for using value of equation in our required place.
x=1
eval(x+1)

"""exec use for exicute program."""                                                          """ ***********""""
exec()

#for filtering our list as our requirment then this functin use.
#we give two arguments first is our requirment and second is function.
filter(none,listig)

#formating ingiventype.
#for we giveour formating arguments and the method (where we convert it.)
"""[[fill]align][sign][#][0][width][,][.precision][type]
where, the options are
fill        ::=  any character
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"     """
format(234,'b')

#frozenset is transform in immutable frozenset with given iterable.
a=['as',2,'d']
frozenset(a)

#getattr is use for returning value from object.
#it has three paramiter and first is give the name of object.
#Second is name of function which we called here.
#in case of function is not in object than, it take this value as defaule, unless it give error.
class a:
    f = 'same'

print(getattr(a,'f','det'))

#global is use for using the global dictionary of we made in program starting.
global()

#hasatrr use for finding the functin name of object is alive or not and then give True orFalse.
hasatrr(a,'e')

#hash keyword using for transforming other values key in intiger value.
hash(34.55)

#help is use for geting help when, we can not understand any function.
help(hash)

#finding uniqe id of given argument id function work.
id(5)

#isinstance is compaer two function and their alements or thier iterable same, then it give true.
isinstance (f,a)

#if class is subclass or it tuples then it give true,unless false.
class b:
    s='as'
issubclass(a,b)

#iter is split class memobers and first time use it return first member and it again ask so give second number. Ths loop continu untill members are not over and after thai it show error.
a=[4,5,6]
b=iter(a)
print(next(b))
#locals is use in only in thir object.
locals()

#map function is comanly use two argument first is with variabl and second argument's variable add in first argument.
#map function return value in lameda so it requires to convert in anyiterabke function.
a=[4,5,6]
b[5,4,3]
f=map(c,d=a+b,a,b)
print(f)
print(set(f))

#this function is used for finding between the passing vaue.
#As well, if compare  variable of intiger, in that time we should give key reffrence for comparing and finding vaue.

def sum(a):
    b=a+5
    return b
a1= [2,3,4,5]
b1=[34,4,1,0]
print(max(a1,b1,key=sum)

                                                                    """*******************"""
memoryview()


#min works like a max but, it returns only minimum value.
def sum(a):
    b=a+5
    return b
a1= [2,3,4,5]
b1=[34,4,1,0]
print(min(a1,b1,key=sum))

#next keyword use for print other value than,iter.And the if we give difautl value,than the error is not showed.
print(next(a,34))

                                        """*************"""
object()

"""Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
buffering (optional) - used for setting buffering policy
encoding (optional) - name of the encoding to encode or decode the file
errors (optional) - string specifying how to handle encoding/decoding errors
newline​ (optional) - how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'
closefd (optional) - must be True (default) if given otherwise an exception will be raised
opener (optional) - a custom opener; must return an open file descriptor"""

#open is used for run or open the file.
open('list.py')

#pow function return the power of first value behalf of second value,and third value is optional and if third value givenso, pow function first get power of first two welue and module with third value.
pow(2,3,4)

                                                                                           """**************************"""                                                                 
property()
    
#it gives range of given arguments.
print(list(range(34,89,2)))

#repr is return same object of string but in printable maneor.
print(repr('animesh')) #answer is " ' animesh ' "

#it basicaly reverse our argument and it can return in given iterator function also.
print(list(reversed(rnge(3,6))))

#this function give round up value of pased argunment and we should also set limit of how many digits round up.
round(45.6787945768989,3)

#setattr function is modified of our class value.
#and it takes three arameters first is object of class, second is function of additing and third is new value.

class name:
      ba = 'and'

c = name()
print(setattr(c,ba,'or'))

#slice function is split of our argument and it required two arguments first starting position and secon is ending position if, we want step in that so weadd third value in function for stepup.
c='animesh'
print(c(slice(3,7,1)))

#staticmethod work for calling class and its object in main body.       """*******************************@"""
staticmethod()

#sum method do sum of iterable object's value and if we add other argument so the sum is starting with our argument.
3 = [23,34,-8.8]
print(sum(3,4))

#super method help for call parent class in based class.
super('parent class function' , 'object')
      
#type function help for finding type of variable.
type(c)

#vars function is give dictionary object if the object is dict object syntex.
s=[a=23,b=45]
print(vars(s))

#zip function is take arguments in itrables and it return in tuples .as well it work for joint one or mre iterables in single tuple.
zip(a1,b1)

#for imprting values in global or localy for that time it is used.
_import_()
      























      
      
