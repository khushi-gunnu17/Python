
'''
>>> f = open('code.py') 
>>> f.readline()
'import time \n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("Code is here.")\n'
>>> 
>>> f.__next__()
'\n'
>>> f.__next__()
'username = "Khushi"\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration




>>> for line in open('code.py') :
...     print(line)
... 
import time 



print("Code is here.")



username = "Khushi"



print(username)






>>> for line in open('code.py').readlines() :
...     print(line, end = " ") 
...
import time

print("Code is here.")

username = "Khushi"

print(username)




>>> f = open('code.py')                       
>>> while True : 
...     line = f.readline()
...     if not line : break
...     print(line, end = " ") 
...
import time

print("Code is here.")

username = "Khushi"

print(username)






>>> test = "Khushi"
>>> if not test : 
...     print("Code")
...
>>> test = ""         
>>> if not test :     
...     print("Code")
...
Code






# with arrays 


>>> myList = [1, 2, 3, 4]
>>> I = iter(myList) 
>>> I
<list_iterator object at 0x000001FE2194E050>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x000001FE2194E050>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration




# for file and not list, the iter object is same as the referenced object

>>> f = open('code.py') 
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> myNewList = [1, 2, 3]
>>> iter(myNewList) is myNewList
False







>>> D = {"a" : 1, "b" : 2}
>>> for key in D.keys() :
...     print(key)
...
a
b
>>> I = iter(D) 
>>> I
<dict_keyiterator object at 0x000001FE2164DCB0>
>>> I.__next__()
'a'
>>> next(I)   
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration





# this shows range is an iterable object

>>> range(5) 
range(0, 5)
>>> R = range(5) 
>>> I = iter(R) 
>>> next(I) 
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

'''