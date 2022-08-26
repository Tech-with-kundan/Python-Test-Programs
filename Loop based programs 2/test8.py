#8. Write a python script to print first N terms of a Fibonacci series
N =  int (input(" enter the term of fibonacci series "))
term1=0
term2=1
print(term1 , end=" ")
print(term2, end=" ")
i=2
while i< N :
    term3= term1+ term2
    print(term3, end=" ") 
    term1= term2; 
    term2= term3 
    i+=1


