#2. 2. Write a python script to calculate sum of squares of first N natural numbers
cal=0; 
n= int(input("enter the number"))
ran= range(1, n+1, 1)
for e in ran:
    cal+=(e**2)

print("the sum of all natural number is ", cal)