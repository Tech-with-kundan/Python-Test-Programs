#2. Write a python script to check whether a given number is Prime or not
num= int(input("enter the number"))
i=2
while i< num:
    if num % i == 0:
        print("NOT PRIME")
        break
    i+=1
else:
    print("PRIME") 