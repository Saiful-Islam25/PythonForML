def reverse(str):
    str1=""
    
    for i in str:
        str1=i+str1
    return str1

str=input("Enter a string : ")
print("The original string is : ",str)
print("The reverse string is",reverse(str))