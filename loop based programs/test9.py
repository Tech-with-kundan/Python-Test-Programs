#9. Write a python script to print binary equivalent of a given decimal number. (do not
#use bin() method)
# look  here is constraint given that you can use inbuilt function . 
def reverse(string):
    string = string[::-1]
    return string


string =""
n= int(input("enter the number: "))
while n>0 :
    rem=n%2
    string+=str(rem)
    n//=2

print(reverse(string))


