#6. Write a python script to print first N prime numbers
num= int(input("enter the number"))

i=2  
cal=0;
while  True :
    j=2
    while j<i:
        if i % j == 0 :
            break
        
        j+=1
    else :
        print(i, end=" ") 
        cal+=1
    if cal == num:
        break
          

        
    i+=1