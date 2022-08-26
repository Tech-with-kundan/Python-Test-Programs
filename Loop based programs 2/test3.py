#3. Write a python script to print all Prime numbers under 100
i=2
num=100
while i< num:
    j=2
    while j<i:
        if i % j ==0 :
            break
        
        j+=1
    else :
        print(i, end=" ") 
        
    i+=1

    