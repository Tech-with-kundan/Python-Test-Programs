"""
10. Write a Python script to create a list, where each element of the list is a digit of a
given number.

"""
mylist=[] # this is an empty list in which I am gonn to ask to the user  for intering the data into the list . 
num=int(input("enter the list size"))
j=0
print("enter the digits as you want ")
while j< num :
    n=int(input())
    mylist.append(n)
    j+=1


print(mylist) 
