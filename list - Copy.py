# list

l=[1,23,45,67,23]

""" append
    minimum one argument
    use for adding value in last. """
l.append(2)
print(l)

""" clear
    clearing whole list."""
l.clear()
print(l)

l=[1,23,45,67,23]

""" copy
    copy list.
    It is also used for deep copy after pop also, all variable in copy variable which call, deep copy """
a=l.copy()
print(l)

""" count
    counting how many of numbers are"""
l.count(23)
print(l)

""" Extend
    use for aditing string with extend it in the word."""
l.extend('animesh')
print(l)

""" Index
    finding position of argument."""
l.index(1)
print(l)

""" insert
    insert value in the list
    give position and new vaue."""
l.insert(3,67)
print(l)

""" pop
    last value of list will delete"""
l.pop()
print(l)

""" remove
    atleast takng one argument
    removeing argument of list."""
l.remove(45)
print(l)

""" reverse
    set arguments in desseding order."""
l.reverse()
print(l)

l=[1,23,45,67,23]

""" sort
    set arguments in asseding order."""
l.sort()
print(l)
