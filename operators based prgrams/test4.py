"""
4 . Write a python script to print greater between two numbers. Print number only once
    even if the numbers are the same.
"""
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if num2> num1 :
    print(num2, " is greater ")
elif num1==num2:
    print("both number are same", num1,"and", num2)
else :
    print(num1," is greater")
