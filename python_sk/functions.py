# in - built functions
# module functions
# User defined functions

# in - built
int()
bool()

# module
import math
print(dir(math))

from math import sqrt
print(sqrt(16))
from math import *

# user defined 
# def function_name(parameters) :
    # do something


def print_sum(first, second) :
    print(first + second)
          
print_sum(1, 4)