def reverse(str):   
    string = "".join(reversed(str))  
    return string   
  
s = input("Enter a string : ") 
  
print ("The original string is : ",s)   
print ("The reversed string using reversed() is : ",reverse(s) )  