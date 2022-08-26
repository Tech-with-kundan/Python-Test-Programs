#10. Write a python script to calculate HCF of two numbers
i=1
num1= int (input("enter the number"))
num2=int(input("enter the number"))
HCF=1
a=1
#  Here I have written double approach of finding HCf of two numbers. 


while i <= num1 and i<= num2 : 
   if num1 % i ==0 and num2 % i ==0 :
        H=i
   i+=1
   
print('the hcf is ', H)

"""
while num1 !=0 :
    a=num1
    num1= num2 % num1 
    num2= a  
print("The HCF of two number is ", num2 )
"""
