"""
6. Write a python script to check whether a given number is a three digit number or not.
"""
num= int(input("enter the number:"))
x=num//100
if x==0:
    print("this number has not three digit ")
else:
    print("yes this is three has more than or equal to three digit ")

