#5. Write a python script to find next prime number of a given number

num2=int(input("enter the number"))
i=num2+1
while i>0:
    j=2
    while j<i:
        if i % j ==0 :
            break
        
        j+=1
    else :
        print(i, end=" ") 
        break
        
    i+=1