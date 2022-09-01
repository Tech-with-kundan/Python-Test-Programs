"""
8. Write a Python script to print distinct elements along with their frequencies of
    occurrence in the list.

"""
listitem=[1,2,3,2,3,2,1,4,5,6,4,5,7,7,8,5,5,5,5]
listitem.sort()
index=0
size=len(listitem)
while index < size:
    k=index+1
    n=listitem.count(listitem[index])
    while k < size and listitem[k]== listitem[index] :
        k+=1
    print(listitem[index],"->",n)
    index=k     


