#7. Write a python script to check whether a given pair of numbers are co-Prime
# numbers or not.
# let's find the  HCF if the HCF  is both  have 1 then we can  call it the number is co-prime otherwise not 
#let's find out the HCF of these two   number . 
i=1
num1= int (input("enter the number"))
num2=int(input("enter the number"))
HCF=0;
while i< num1 and i< num2 :
    if num1 % i  ==0 and  num2 % i ==0 :
        HCf=i
    i+=1

if HCf == 1 :
    print("Co-prime Number")
else:
    print("NOt co- prime number")

      
