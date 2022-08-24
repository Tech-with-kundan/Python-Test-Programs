"""
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""
from os import system
# wow this is power of python programming language . 
while (True) :
    system("cls")
    print("\na. Check for isosceles triangle")
    print("\nb. Check for right angle triangle")
    print("\nc. Check for equilateral triangle")
    print("\nd. exit........")
   
    choice=input("enter your choices")

    match choice :
        case "a":
            side1=int(input("enter the  first side of triangle: "))
            side2=int(input("enter the  second  side of triangle: "))
            side3=int(input("enter the  third  side of triangle : "))
            if side1 == side2  or  side1  == side3 or side2 == side3 :
                print("Isosceles triangle")
                input()
            else:
               print("Not isosles triamgle")
               input()  
          
            
        case "b":
            side1=int(input("enter the  first side of triangle"))
            side2=int(input("enter the  second  side of triangle"))
            side3=int(input("enter the  third  side of triangle"))
            if side1 == 90 or  side2==90 or side3==90 :
                print("Right angle  triangle")
                input()
            else:
               print("Not  Right angle  triamgle")
               input()  
          
            
             
        case "c":
            side1=int(input("enter the  first side of triangle"))
            side2=int(input("enter the  second  side of triangle"))
            side3=int(input("enter the  third  side of triangle"))
            if side1 ==  side2 and side2 == side3 :
                print("Equilateral triangle ")
                input()
            else:
               print("Not Equilateral triangle ")
               input()  
          
        case "d":
            print("ThankYou\n press any key to exit")
            input()
            exit(0)
        case _ :
            print("invalid choice")
            input();
 

             

