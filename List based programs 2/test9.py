"""
9. Write a Python script to print indices of all occurrences of a given element in a given
     list.

"""
N=int (input("enter the   list size"))
element=int(input("enter the element "))
r= 0
Naturallist=[]
print("enter the list item : ")
while r < N :
    n=int(input())
    Naturallist.append(n)
    r+=1
index=0
print("the occurence element 's  indexes are ")
while( index < N ):
    if(Naturallist[index] == element) :
        print(index )
    index+=1





