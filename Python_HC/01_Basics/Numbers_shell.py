'''

>>> x = 2
>>> y = 3
>>> z = 4
>>> x + y
5
>>> x + y * z
14
>>> (x + y) * z 
20
>>> 40 + 2.23
42.23
>>> 'khushi' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int(2.23)
2
>>> float(40) 
40.0

# operator overloading, concatenating
>>> 'khushi' + 'sharma' 
'khushisharma'


>>> x, y, z
(2, 3, 4)
>>> x + 1, y * 2
(3, 6)
>>> 100 ** 2
10000
>>> 2 ** 100
1267650600228229401496703205376
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> 100 ** 100
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> result = 1/3.0
>>> result
0.3333333333333333


>>> repr("Khushi") 
"'Khushi'"
>>> str('Khushi') 
'Khushi'
>>> print('Khushi') 
Khushi


>>> 1 < 2
True
>>> 5.0 == 5.0
True
>>> 4.0 != 5.0
True
>>> x, y, z
(2, 3, 4)
>>> x < y < z
True
>>> x < y and y < z
True
>>> x < y or y < z  
True


>>> 1 == 2 < 3
False
>>> 1 == 2 and 2 < 3
False
>>> import math
>>> math.floor(3.5) 
3
>>> math.floor(-3.5) 
-4

# trunc takes you towards the 0 in the number line
>>> math.trunc(5.8) 
5
>>> math.trunc(-5.8) 
-5
>>> 999999999999999999999999999999 + 1
1000000000000000000000000000000
>>> 999999999999999999999999999999999 * 2.1
2.1e+33
>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376



>>> 2 + 1j
(2+1j)
>>> 2 + 1j * 3
(2+3j)
>>> (2 + 1j) * 3 
(6+3j)
>>> 0o20
16
>>> 0xFF
255
>>> 0b10000
16
>>> oct(64) 
'0o100'
>>> hex(64) 
'0x40'
>>> bin(64) 
'0b1000000'

>>> int(64)
64
>>> int('64', 8) 
52
>>> int('64', 16) 
100
>>> int('64', 2)  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 2: '64'
>>> int('1000', 2) 
8



>>> x = 1
>>> x << 1
2
>>> x << 2
4
>>> x | 2
3



>>> import random
>>> random.random()
0.7509547998353179
>>> random.randint(1, 101) 
46
>>> random.randint(1, 101)
11
>>> random.randint(1, 101)
12
>>> random.randint(1, 101)
76
>>> l1 = ['one', 'two', 'three', 'four'] 
>>> random.choice(l1) 
'three'
>>> random.shuffle(l1)
>>> l1
['two', 'three', 'one', 'four']




>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3 
5.551115123125783e-17
>>> from decimal import Decimal 
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') 
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') 
Decimal('0.0')

# Decimal context manager = can read more here 


>>> from fractions import Fraction
>>> myFraction = Fraction(2, 7)
>>> myFraction                 
Fraction(2, 7)



>>> setone = {1, 2, 3, 4} 
>>> setone & {1, 3} 
{1, 3}
>>> setone | {1, 3} 
{1, 2, 3, 4}
>>> setone | {1, 3, 7} 
{1, 2, 3, 4, 7}
>>> setone 
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4} 
set()
>>> type({}) 
<class 'dict'>



>>> type(True) 
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> False is 0
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True + 4
5
>>> 5 * False 
0


'''