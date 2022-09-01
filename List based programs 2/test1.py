"""
1. Write a Python script to create a list of first N natural numbers.

"""
N=int (input("enter the number"))
r= range(1,N+1,1)
Naturallist=[]
for e in r :
    Naturallist.append(e)
print(Naturallist)


