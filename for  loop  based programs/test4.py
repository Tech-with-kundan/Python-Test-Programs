#4. Write a python script to print first N odd natural numbers
N= int(input("enter the number"))
ran= range(1,2*N, 2)
for e in ran:
    print(e, end=" ")
    