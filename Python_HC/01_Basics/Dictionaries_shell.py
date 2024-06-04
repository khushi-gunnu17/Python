'''

>>> chai_types = {"Masala" : "Spicy", "Ginger" : "Zesty", "Green" : "Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger") 
'Zesty'
>>> chai_types.get("Gingery") 
>>> chai_types["Masalaa"]     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Masalaa'
>>> chai_types["Green"] = "Fresh" 
>>> chai_types                
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types : 
...     print(chai) 
... 
Masala
Ginger
Green




>>> for chai in chai_types : 
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key, values in chai_types.items() :  
...     print(key, values)
... 
Masala Spicy
Ginger Zesty
Green Fresh
>>> if "Masala" in chai_types :
...     print("I have Masala Chai")
...
I have Masala Chai
>>> print(len(chai_types))
3






>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy = chai_types.copy()





>>> {{}, {}, {}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'





>>> tea_shop = {
... "chai" : {"Masala" : "Spicy", "Ginger" : "Zesty"},
... "Tea" : {"Green" : "Fresh", "Black" : "Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Fresh', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"] 
'Zesty'






>>> squared_num = {x : x**2 for x in range(6)} 
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}
>>> keys = ["Masala", "Ginger", "Lemon"]
>>> keys   
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value) 
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)          
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}

'''