"""
2. Write a Python script to create a list of first N odd natural numbers.

"""
N=int (input("enter the number"))
r= range(1,2*N+1,2)
Naturallist=[]
for e in r :
    Naturallist.append(e)
print(Naturallist)
