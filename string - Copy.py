f = 'hello world'

"""capitalize
    first word transform in capital alphabet."""
f.capitalize()

"""casefold
    transfer whole string in small alphabets.""" 
f.casefold()

""" center
    one argument give
    use for puting space ."""
f.center(34)

""" count
    counting position of string's arguments."""
f.count('h')

""" encode use for finding position in unicode-8."""
f.encode()

""" endswith use for finding our entering value is last in string or not."""
f.endswith('d')

""" expandtabs use for spending tabs."""
f.expandtabs(5)

""" findind the position of searching argument."""
f.find(h)

""" format using for edit value in string .
    it requiered two arguments forst where and what value.
    In string we must mantion the place in curlibraket."""
s = 'My name is{age: } animesh.'
s.format(age = 18)

""" format_map  """                                                         #***************
f.format_map()

""" index useing for finding position of arguments and its required one argument."""
f.index('o')

""" if string is alphabetical+numberic than gives true unless, fallse."""
f.isalnum()

"""if string is only  alphabatical then give true."""
f.isalpha()

""" if string """                                                           #************************
f.isascii()

""" if all are numeric and the are without point number, then give true."""
f.isdecimal()

""" if all are digits then give true.""" 
f.isdigit()

""" if string is identifier."""                                             #************
f.isidentifier()

""" if string write in lower case then, give true."""
f.islower()

""" if strings' all charecters are numeric so, giv true.""""  
f.isnumeric()

"""string's all cheracters are pirntable so ,it give true."""
f.isprintable()

""" in string creat with space, then give true."""
f.isspace()

""" string is true if string follw the rules of title."""
f.istitle()

""" string write in upper case then, it gives true."""
f.isupper()

"""join use for editing in collection datatype  and edd string between the paramiters of collection datatypes."""
d=['sa','df','ght']
e=' & '
e.join(d)


""" use for ading space or character in left side . In case of, adding character we first give nmber and then , character.""" 
f.ljust(23,'o')

""" use for making all characters in lower alphabates."""
f.lower()

"""use for  removing unwanted characters in strings.
    It required one character or it takes space as default."""
f.lstrip(l)

                                                                    #*****************************
f.maketrans()

""" transform strings in tuple."""
f.partition()

"""use for replaceing words.
    it takes two argument first for replacing word and second is new word.""""
f.replace(hello,hi)

"""use for finding position of given argument .and it give last position of arguments."""
f.rfind('o')

""" work like a function of rfind."""
f.rindex('i')

""" use for ading space or character in right side . In case of, adding character we first give nmber and then , character.""" 
f.rjust(23,'o')

""" use for partition in string. and it count last word of string and after that, it break the string .It requireds one argument."""
f.rpartition(o)

""" It works for split strings with our arguments. If maximum given then it split only that time unless it split maximum time.""""
f.rsplit(',',1)

"""removing character or space of given if, not mantion then, it takes space as a default."""
f.rstrip('i')

""" useing for split strings with given characters. And character is compulsoary part of string.""" 
f.split(w)

"""split with lines and the line is comulsory part of string."""                            #********** 
f.splitlines()

""" string starting with given arguments, then it give true.""" 
f.startswith('h')

"""use for remooving all kind of stuf and it not matered with order."""
f.strip('hw')

"""use for transfor upercase to lowercase and vice versa also True."""
f.swapcase()

"""use for capitalize first key word of every word."""
f.title()

                                                                                    #**************
f.translate()

""""transform all characters in capitalization."""
f.upper()

""""zfill transform the numbers of total arguments wich, we given.And the strings characters are not sufficient In that case, it add some zero in right side.""" 
f.zfill(59)
         
