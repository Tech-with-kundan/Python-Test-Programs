#7. Write a python script to print first N  even natural numbers in reverse order
N=int(input("enter number of times "))
i=1
while i<=N :
    print(2*(N+1- i), end=" ")
    i+=1