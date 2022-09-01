"""
9. Write a Python script to create a list of city names taken from the user.

"""


mylist=[] # this is an empty list in which I am gonn to ask to the user  for intering the data into the list . 
num=int(input("enter the list size"))
j=0
print("enter the city names as you want ")
while j< num :
    n=input()
    mylist.append(n)
    j+=1


print(mylist) 
