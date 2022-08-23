"""
10. Write a python script to print greater among three numbers. Print number only once
     even if the numbers are the same.
"""
num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if num1>num2:
    if num1>num3:
        print(num1, " is greater amoung these three number")
    else:
        print(num3, " is greater amoung these three number")
else:
    if num2>num3:
        print(num2, " is greater amoung these three number")
    else:
        print(num3, " is greater amoung these three number")
