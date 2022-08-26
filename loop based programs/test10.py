#10. Write a python script to print the octal equivalent of a given decimal number. (do not
#use oct() method)
def reverse(string):
    string = string[::-1]
    return string


string =""
n= int(input("enter the number: "))
while n>0 :
    rem=n%8
    string+=str(rem)
    n//=8

print(reverse(string))