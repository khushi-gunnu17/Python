

'''

>>> tea_varities = ["Black", "Green", "Oolong", "White"] 
>>> tea_varities                                        
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0]) 
Black
>>> print(tea_varities[-1]) 
White
>>> print(tea_varities[1:3]) 
['Green', 'Oolong']
>>> print(tea_varities[:2])  
['Black', 'Green']
>>> print(tea_varities[::2]) 
['Black', 'Oolong']
>>> tea_varities[3] = "Herbal" 
>>> print(tea_varities)        
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varities[1:2] 
['Green']
>>> tea_varities[1:2] = "Lemon"
>>> tea_varities               
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varities[1:2] = ["Lemon"]           
>>> tea_varities
['Black', 'Lemon', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']





>>> tea_varities = ["Black", "Green", "Oolong", "White"]
>>> tea_varities[1:2]          
['Green']
>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3] = ["Green", "Masala"]
>>> tea_varities
['Black', 'Green', 'Masala', 'White']




>>> tea_varities[1:1] 
[]
>>> tea_varities[1:1] = ['test', 'test']
>>> tea_varities      
['Black', 'test', 'test', 'Green', 'Masala', 'White']
>>> tea_varities[1:2]
['test']
>>> tea_varities[1:3]     
['test', 'test']
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'Green', 'Masala', 'White']




>>> tea_varities = ["Black", "Green", "Masala", "White"] 
>>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> for tea in tea_varities :
...     print(tea)
... 
Black
Green
Masala
White
>>> for tea in tea_varities :
...     print(tea, end = " ")
... 
Black Green Masala White >>> 
>>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> if "Oolong" in tea_varities :
...     print("I have Oolong tea.") 
... 
>>> 
>>> tea_varities.append("Oolong")   
>>> tea_varities                    
['Black', 'Green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in tea_varities :
...     print("I have Oolong tea.")
...
I have Oolong tea.





>>> tea_varities.pop()              
'Oolong'
>>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> tea_varities.remove("Green") 
>>> tea_varities
['Black', 'Masala', 'White']
>>> tea_varities.insert(1, "Green") 
>>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> tea_varities_copy = tea_varities.copy()
>>> tea_varities_copy.append("Lemon") 
>>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> tea_varities_copy                       
['Black', 'Green', 'Masala', 'White', 'Lemon']

'''




# List comprehension

'''
>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [x**3 for x in range(1, 6)]
>>> cube_num   
[1, 8, 27, 64, 125]

'''




'''
zip method 

x = [("Apple", 50000), ("Dell", 30000)]
laptop, price = zip(*x)
print(laptop, price)




tup = (1, 2, 3)
my_list = [5, 6, 7]

l = list(zip(tup, my_list))
print(l)

d = dict(zip(tup, my_list))
print(d)

'''