#4. Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)
num1=int(input("enter the number"))
num2=int(input("enter the number"))
i=num1+1
while i< num2:
    j=2
    while j<i:
        if i % j ==0 :
            break
        
        j+=1
    else :
        print(i, end=" ") 
        
    i+=1