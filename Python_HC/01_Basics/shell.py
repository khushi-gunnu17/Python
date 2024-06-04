# while writing new code in the file, you cannot access the new written code from the file to the terminal where you have imported it, you need to rerun the import statement

'''
>>> print("Khushi")
Khushi

# built-in calculator in python
>>> 2 * 2
4

>>> "Khushi " * 4
'Khushi Khushi Khushi Khushi '

>>> score = 100
>>> score
100

>>> tea     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea' is not defined

>>> import os
>>> os.getcwd()
'C:\\Users\\vs\\OneDrive\\Desktop\\Python_HC\\01_Basics'

>>> for c in "Khushi":
...     print(c)
...
K
h
u
s
h
i

>>> import sys
>>> sys.platform
'win32'

>>> import hello_python
Hello Python
4
Khushi Sharma

>>> hello_python.khushi("Khushi Sharma")  
Khushi Sharma

>>> hello_python.khushi_one             
'Khushi Sharma'


>>> hello_python.khushi_four
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'hello_python' has no attribute 'khushi_four'. Did you mean: 'khushi_one'?

>>> from importlib import reload 
>>> reload(hello_python)
Hello Python
4
Khushi Sharma
<module 'hello_python' from 'C:\\Users\\vs\\OneDrive\\Desktop\\Python_HC\\01_Basics\\hello_python.py'>

>>> hello_python.khushi_four     
'Khushi Jangid'

'''


# Immutable and mutable

'''
>>> username = "Khushi"
>>> username   
'Khushi'
>>> username = "Khushi Sharma"
>>> username
'Khushi Sharma'


>>> x = 10
>>> y = x
>>> x
10
>>> y
10
>>> x = 15
>>> y
10

'''


# Datatypes

'''
>>> mylist = [1, 2, 3, ['a', 'b']]
>>> mylist[2] 
3
>>> mylist[3] 
['a', 'b']
>>> dict(hours = 10)
{'hours': 10}



>>> 12 + 12
24
>>> 2.5 * 5
12.5
>>> 2 ** 100
1267650600228229401496703205376
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.9471079621207827
>>> random.choice([1, 2, 3, 4, 5, 6]) 
5
>>> random.choice([1, 2, 3, 4, 5, 6])
2
>>> username = "Khushi Sharma"
>>> len(username)  
13
>>> username[0]
'K'
>>> username[0] = 't' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> username[-1]     
'a'
>>> username[1:3]
'hu'


>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



>>> mylist = [123, 'chai', 3.14]
>>> mylist                      
[123, 'chai', 3.14]
>>> len(mylist)
3
>>> mylist[-1]  
3.14
>>> myD = {"one" : "Lemon Tea", "Two": "Ginger", 'Three' : "Superman"}
>>> myD
{'one': 'Lemon Tea', 'Two': 'Ginger', 'Three': 'Superman'}
>>> myD['one']
'Lemon Tea'
>>> myD['four']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'four'
>>> myTup = (1, 2, 3, 4)
>>> myTup[0]
1
>>> len(myTup)
4



'''



# ref_count = the count of reference variables for a value.

# there is no datatype assigned to the variable, but the memory reference is assigned the datatype.

# there are pointers in python also.

# Python doesn't immediately does the garbage collection of Numbers and Strings. But There can be forceful collection also. 

# deepcopy for copying all the lists within a list into some other list
# - import copy
# - h2 = copy.deepcopy(h1)
# h2 = copy.copy(h1)  is same as h2 = h1[:]


# Memory reference Understanding

'''
>>> import sys
>>> sys.getrefcount(24601)
3
>>> sys.getrefcount('khushi') 
4294967295
>>> sys.getrefcount(1)        
4294967295

>>> a = 3
>>> a = "Khushi sharma"
>>> a = 3.14
>>> type(a)
<class 'float'>
>>> a = 5
>>> b = 2
>>> a
5
>>> b
2
>>> a = a + 2
>>> a
7



>>> myListOne = [1, 2, 3]
>>> myListTwo = myListOne 
>>> myListOne = 'Khushi'  
>>> myListTwo            
[1, 2, 3]
>>> myListOne = [1, 2, 3] 
>>> myListTwo
[1, 2, 3]
>>> myListOne[0] = 33   
>>> myListOne        
[33, 2, 3]
>>> myListTwo
[1, 2, 3]



>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0] = 44
>>> l2
[44, 2, 3]




>>> h1 = [1, 2, 3]
>>> h2 = h1[:]   
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0] = 55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]

# same as the above copy of the h2 by slicing
>>> import copy
>>> h2 = copy.copy(h1)
# gives nested copy of the list
>>> h2 = copy.deepcopy(h1)



# is checks the memory reference of the two objects.
>>> n = [1, 2, 3]
>>> m = n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m == n
True
>>> m is n 
True
>>> m = [1, 2, 3]
>>> m == n        
True
>>> m is n 
False


'''

# dynamic reference type