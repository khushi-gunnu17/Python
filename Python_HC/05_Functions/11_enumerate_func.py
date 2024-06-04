# In Python, the enumerate() function is used to add a counter to an iterable object (like a list, tuple, string, etc.) and returns an enumerate object. This object yields pairs containing a count (starting from zero by default) and the values obtained from the iterable.

# enumerate(iterable, start=0)


fruits = ['apple', 'banana', 'orange']

# for index, fruits in enumerate(fruits) :
#     print(index, fruits)


# for index, fruits in enumerate(fruits, start = 1) :
#     print(index, fruits)


indexed_fruits = {index : fruit for index, fruit in enumerate(fruits)}
print(indexed_fruits)







# Python's enumerate method allows you to iterate over a list, tuple, or dictionary and return a tuple containing the index of each element and the element itself. This is a convenient way to keep track of both the element and its position on a list.

'''
>>> x = ('Masala', "Ginger", "Lemon")     
>>> y = enumerate(x)
>>> y
<enumerate object at 0x000001A00A1CDDA0>
>>> list(y)
[(0, 'Masala'), (1, 'Ginger'), (2, 'Lemon')]
'''
