"""
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
   is even, print Prateek Jain if the number is negative odd number and print Aditya
   Choudhary if number is positive odd number.

"""
number= int (input("enter the number "))
if number % 2 ==0 :
    print("Saurabh shukla")
else : 
    if number > 0 :
        print("Aditiya Choudhary")
    else :
        print("Prateek jain")

