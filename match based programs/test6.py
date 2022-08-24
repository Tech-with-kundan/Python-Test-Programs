"""
6. Write a python program to check whether a given string is a multiword string or single
   word string using match case statement
"""
word= input("enter the world ")
id=0
if " " in word :
    id=1
match id:
    case 1:
        print("yes Multiword is present in the string  ")
    case 0:
        print("Multi word is not present in the string ")
    