#3.3. Write a python script to calculate sum of cubes of first N natural numbers

cal=0; 
n= int(input("enter the number"))
ran= range(1, n+1, 1)
for e in ran:
    cal+=(e*e*e)

print("the sum of all   cubes natural number is ", cal)
