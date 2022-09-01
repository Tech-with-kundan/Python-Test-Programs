"""
3. Write a Python script to create a list of first N even natural numbers.
"""
N=int (input("enter the number"))
r= range(2,2*N+2,2)
Naturallist=[]
for e in r :
    Naturallist.append(e)
print(Naturallist)