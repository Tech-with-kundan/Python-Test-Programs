from ensurepip import version


## in the python we have different ways to print the version of it 
## whether we can use commamd line, or through manually 
## let's see 
## using command lind we have  just write python version  -V 
""""
 In order to print the python version we will have to import a files is called sys . 
 the then we have call the version   via . dot operator . 
"""
import sys
print("User Python version is ", sys.version)