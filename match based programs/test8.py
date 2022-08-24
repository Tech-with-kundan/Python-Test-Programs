"""
8. Write a python script to check whether two given strings are identical, first string
   comes before the second in dictionary order or first string comes after the second 
   string in dictionary order using match case statement
"""
word1= input("enter the first word:")
word2= input("enter the second word:")
match word1<word2:
    case 1:
        print("dictionary order")
    case 0:
        print("Not dictionay order")



