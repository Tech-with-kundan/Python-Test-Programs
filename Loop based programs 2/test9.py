#9. Write a python script to calculate LCM of two numbers
num1= int (input("enter the  first number"))
num2= int (input("enter the second number "))
i=2
lcm=1
ans=0
if num1>num2:
    ans=num2
else:
    ans= num1 
while i <= ans  :
    if num1 % i == 0 and num2 % i == 0 :
        num1//=i
        num2//=i
        lcm *= i
    else:
        i+=1
print("the LCM of two number is ", lcm * num1 * num2 )



