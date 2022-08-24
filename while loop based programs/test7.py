"""
7. Write a python program to check whether a given number is positive, negative or
   zero using match case statement
"""
num= int(input("enter the number"))
match num>0:
   case 1:
    print("Positive")
   case 0 :
      if num==0 :
         print("zero")
      else :
         print("Negative")


