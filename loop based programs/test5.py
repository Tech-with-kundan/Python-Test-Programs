#5. Write a python script to calculate sum of first N even natural numbers
cal=0; 
n= int(input("enter the number"))
ran= range(1, n+1, 1)
for e in ran:
    cal+=(e*2)

print("the sum of  even   natural number is ", cal)