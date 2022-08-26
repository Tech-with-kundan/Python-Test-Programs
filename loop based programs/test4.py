#4. Write a python script to calculate sum of first N odd natural numbers

cal=0; 
n= int(input("enter the number"))
ran= range(1, n+1, 1)
for e in ran:
    cal+=(e*2-1)

print("the sum of odd  natural number is ", cal)