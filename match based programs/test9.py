"""
9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
"""
year= int (input("enter the year: "))
match year % 4==0 and year % 100 != 0 or year % 400 == 0 :
    case 1:
        if(year % 100  == 0  ):
            print(" Century leap year ")
        else :
             print(" Non Century leap year ")


    case 0:
        if(year % 100  == 0  ):
            print(" Century non  leap year ")
        else :
             print(" Non Century  non leap year ")
        