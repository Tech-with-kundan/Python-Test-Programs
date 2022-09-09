"""
9. Write a python script to check if a string contains only characters of the alphabet.

"""
from curses.ascii import isalpha


string=input("enter the string")
if string.isalpha():
    print("yes all character are alphabet")
else:
    print("No all the character are not alphabet")
