"""
7. Write a Python script to remove all non int values from a list.

"""
listitem=[True,"Hello",67.88, " Python", 23+7j, 2022]
anslist=[]
for e in listitem:
    if(type(e)==int):
       anslist.append(e)
print(anslist)
    

