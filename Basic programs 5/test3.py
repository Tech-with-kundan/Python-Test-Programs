"""
3. Write a python script to swap data of two variables
"""
num1=int(input("enter the  1st number"))
num2=int(input("enter the 2nd number"))
print("Before swapping the number is ")
print("num1 is ",num1)
print("num2 is ",num2)
num1=num1*num2
num2=num1//num2
num1=num1//num2
print("after swapping the number is ")
print("num1 is", num1)
print("num2 is ", num2)