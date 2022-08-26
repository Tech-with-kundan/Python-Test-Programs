#7. Write a python script to print first N even natural numbers in reverse order
N= int(input("enter the number"))
ran= range(2*N,0,-2)
for e in ran:
    print(e, end=" ")