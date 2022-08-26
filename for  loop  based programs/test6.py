#6. Write a python script to print first N even natural numbers
N= int(input("enter the number"))
ran= range(2,2*N+2,2)
for e in ran:
    print(e, end=" ")