#8. Write a python script to calculate sum of digits of a given number
cal=0; 
n= int(input("enter the number: "))
while n>0 :
    rem=n%10
    cal+=rem
    n//=10

print("the  sum of digit is  ", cal)