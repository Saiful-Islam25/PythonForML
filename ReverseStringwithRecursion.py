def reverse(str):   
    if len(str) == 0:  
        return str   
    else:   
        return reverse(str[1:]) + str[0]   
    
str = input("Enter a string : ")   
print ("The original string  is : ", str)     
print ("The reversed string(using recursion) is : ", reverse(str))  