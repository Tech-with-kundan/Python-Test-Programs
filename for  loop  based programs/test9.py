#9. Write a python script to print cubes of first N natural numbers
N=int(input("enter the number"))
ran= range(N)
for e in ran :
    print((e+1)*(e+1)*(e+1), end=" ")