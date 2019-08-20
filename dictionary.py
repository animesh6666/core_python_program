s = {'sa' : 'asf' , 'age' : 'dsa' , 54 :34}

type(s)

#clear the set.
s.clear()

s = {'sa' : 'asf' , 'age' : 'dsa' , 54 :34}

#copy dictionary in other variable.
b=s.copy()

#two difrent set to combine and add in dictionary, as well diract can add dictionary key and value.
a=('fo','do')
b=('ta','df')
s.fromkeys(a,b)

#get the value of given key.
s.get('sa')

#divid in the set of key and value.
s.items()

#showing keys of dictionary.
s.keys()

#pop the given argument.
s.pop('sa')

#pop the elements and it starting with last.
s.popitem()

#set default as return the value of key. And it also return value if we add both key and value.
s.setdefault('sa')

#use for add the pair of key and value in dictionary
s.update({'both' : 'done'})

#return the value of keys.
s.values()

