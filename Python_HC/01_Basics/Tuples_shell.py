'''
>>> tea_types = ("Black", "Green", "Oolong", "Black") 
>>> tea_types
('Black', 'Green', 'Oolong', 'Black')
>>> tea_types[0] 
'Black'
>>> tea_types[-2] 
'Oolong'
>>> tea_types[1:] 
('Green', 'Oolong', 'Black')
>>> tea_types[3] = "Lemon" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types) 
4



>>> more_tea = ("Herbal", "Earl_grey") 
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl_grey', 'Black', 'Green', 'Oolong', 'Black')
>>> if "Green" in all_tea : 
...     print("I have green tea.") 
... 
I have green tea.
>>> more_tea = ("Herbal", "Earl_grey", "Herbal") 
>>> more_tea.count("Herbal") 
2
>>> tea_types.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'




>>> tea_types      
('Black', 'Green', 'Oolong', 'Black')
>>> (black, green, Oolong, black) = tea_types 
>>> black
'Black'
>>> green
'Green'
>>> type(tea_types) 
<class 'tuple'>
>>> tea = ("", (1, 2, 3), "")
'''
