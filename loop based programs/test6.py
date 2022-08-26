#6. Write a python script to calculate factorial of a given number
cal=1; 
n= int(input("enter the number"))
ran= range(1, n+1, 1)
for e in ran:
    cal*=(e)

print("the  factorial of given number is  ", cal)