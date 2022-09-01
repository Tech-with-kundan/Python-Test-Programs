"""
4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]

"""
mylist=["java","SQL","C","Reactnative","javascript","python"]

length=len(mylist)
j=0
while j< length:
    if(mylist[j]=="SQL"):
        mylist[j]="NoSQL"
    if(mylist[j] == "Reactnative"):
        mylist[j]="Flutter"
    j+=1

print(mylist)   




