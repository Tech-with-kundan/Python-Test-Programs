"""
6. Write a Python script to calculate the sum of elements in a given list of numbers.

"""
N=int (input("enter the   list size"))
r= 0
Naturallist=[]
print("enter the list item : ")
while r < N :
    n=int(input())
    Naturallist.append(n)
    r+=1

print(" the largest value  of this list is " , sum(Naturallist))