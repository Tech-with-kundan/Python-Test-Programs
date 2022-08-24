"""
2. Write a menu driven program to perform following operations - Addition, Subtraction,
   Multiplication, Division
"""
from os import system
# wow this is power of python programming language . 
while (True) :
    system("cls")
    print("\n1.Addition")
    print("\n2.Subtraction")
    print("\n3.Multiplication")
    print("\n4.Division\n\n")
    choice=int(input("enter your choices"))
    if choice < 5 :
        num2 =int(input("enter  the  first  number "))
        num1 =int(input("enter  the  first  number "))
    match choice :
        case 1:
            print("addition =", num1+num2)
            input();
        case 2:
             print("subtraction =", num1-num2)
             input();
        case 3:
             print("multiply =", num1*num2)
             input();
        case 4:
             print("Division =", num1/num2)
             input();
        case 5:
            print("ThankYou\n press any key to exit")
            input()
            exit(0)
        case _ :
            print("invalid choice")
            input();
   # system("cls")

             

