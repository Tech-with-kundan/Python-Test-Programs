#7. Write a python script to count digits in a given number
cal=0; 
n= int(input("enter the number"))
while n>0 :
    cal+=1
    n//=10

print("the  total  digit is present in the number is   ", cal)