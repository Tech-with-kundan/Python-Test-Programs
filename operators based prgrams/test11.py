"""
12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part 

"""

num=complex(input("enter the complex type number "))
#print(num.real)
#print(num.imag)
if num.real > num.imag :
    print(" real part is greater")
else:
    print(" imaginary part is greater")
