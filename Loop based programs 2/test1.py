#1. Write a python script to reverse a number.
n=int(input("enter the number"))
rev=0
while n != 0 :
    rem= n % 10
    rev= rev * 10 + rem 
    n//=10
print("the reverse number is ", rev); 
