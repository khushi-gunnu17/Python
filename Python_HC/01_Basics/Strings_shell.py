# String = Unicode string
# {} = Placeholder for values in formatting

'''
>>> name = "Khushi Sharma"
>>> name
'Khushi Sharma'
>>> print(name)
Khushi Sharma
>>> name = "Khushi Jangid"
>>> first_char = name[0]  
>>> first_char
'K'
>>> print(first_char)
K
>>> sliced_name = name[0:6]
>>> print(sliced_name)   
Khushi
>>> name[-1] 
'd'




>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:] 
'3456789'
>>> num_list[0:7:2] 
'0246'
>>> num_list[0:7:3] 
'036'
>>> num_list[0:7:-1] 
''
>>> num_list[7:0:-1] 
'7654321'




>>> name
'Khushi Jangid'
>>> print(name.lower()) 
khushi jangid
>>> print(name.upper()) 
KHUSHI JANGID
>>> name
'Khushi Jangid'
>>> name = "    Khushi    "
>>> name
'    Khushi    '
>>> print(name.strip()) 
Khushi
>>> name = "Khushi Jangid"
>>> print(name.replace("Khushi", "Gunnu"))
Gunnu Jangid
>>> name
'Khushi Jangid'



>>> name = "Khushi, Gunnu, Gunniya, Gunnushi"
>>> print(name.split())    
['Khushi,', 'Gunnu,', 'Gunniya,', 'Gunnushi']
>>> print(name.split(", "))
['Khushi', 'Gunnu', 'Gunniya', 'Gunnushi']
>>> name = "Khushi Sharma"
>>> print(name.find("Sharma"))
7
>>> print(name.find("sharma")) 
-1
>>> name = "Khushi Sharma Sharma Sharma"  
>>> print(name.count("Sharma")) 
3


>>> name_type = "Gunnu"  
>>> quantity = 2    
>>> order = "I ordered cups of {} from {}"    
>>> order
'I ordered cups of {} from {}.'
>>> print(order.format(quantity, name_type))
I ordered cups of 2 from Gunnu.




>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety)) 
LemonMasalaGinger
>>> print(" ".join(chai_variety))       
Lemon Masala Ginger



>>> name = "Khushi Sharma" 
>>> name
'Khushi Sharma'
>>> len(name) 
13
>>> for letter in name :
...     print(letter) 
...
K
h
u
s
h
i

S
h
a
r
m
a
>>> for letter in name :
...     print(letter, end=" ")
...
K h u s h i   S h a r m a >>>



>>> string = "He said, \"Khushi is insane\". " 
>>> string
'He said, "Khushi is insane". '
>>> string = "Khushi\nSharma"
>>> string
'Khushi\nSharma'
>>> print(string) 
Khushi
Sharma

# Here, r stands for raw string.
>>> string = r"Khushi\nSharma" 
>>> string
'Khushi\\nSharma'
>>> print(string) 
Khushi\nSharma




>>> path = r"c:users/khushi/python" 
>>> path
'c:users/khushi/python'
>>> print(path) 
c:users/khushi/python
>>> path = "c:users/khushi/python"  
>>> print(path)
c:users/khushi/python
>>> path = r"c:users//khushi//python" 
>>> path
'c:users//khushi//python'
>>> print(path)
c:users//khushi//python



# Membership Operators
>>> name = "Khushi Sharma"
>>> print("Gunnu" in name)  
False
>>> print("Khushi" in name) 
True
'''