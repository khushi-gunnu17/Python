# Python's Inner working

> python script.py

converts first script.py into Byte Code (mostly hidden).  
Not completely like java Byte Code.

The Byte Code is then run into the Virtual Machine.

One thing is also installed with Python, Python VM (Virtaul Machine), this machine actually runs the code.

1. Compile to Byte code (low level code amd not machine code which is platform independent)  (compile - Just a term for interpretation term)

-> Byte code runs faster 

.pyc = compiled python(frozen binaries)



## pycache folder
__pycache__

Source Change and Python Version  
hello_python.cpython-312.pyc

- works only for imported files
- not for top level files (when the file is only one)  

we need optimization when there are more than one files if we are importing files into another one.

uses diffing algorithms just like git




## Python Virtual Machine 
- code loop to iterate byte code.
- Run time Engine.
- Also known as __python interpreter__.


## Byte Code
Byte code is __Not__ machine code.  
Machine code is direct instruction for your hardware such as instructions to apple chip.

- Python specific interpretation.
- cpython (standard implementation) , jython/jpython (If you want to work with java binaries) , IronPython, Stackless (for Concurrency), PyPy (Performance Oriented)


## Extra 

hashnode = A famous developer blogging website


Python first watches the current directory while importing from any file in the terminal.


m is n ==> this is used to check the same memory reference of two variables.
