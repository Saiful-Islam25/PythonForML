def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y


print("Select Operation : ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiption")
print("4.Division")


while True:
    choose=input("Enter your choice (1/2/3/4) : ")
    
    if choose in ('1','2','3','4'):
        #try:
            num1=float(input("Enter first number : "))
            num2=float(input("Enter second number : "))

        #except Valueerror:
        
    if choose =='1':
            print(num1,"+",num2,"=",add(num1,num2)) 
            
               
    elif choose =='2':
            print(num1,"-",num2,"=",subtract(num1,num2)) 
               
    elif choose =='3':
            print(num1,"*",num2,"=",multiply(num1,num2)) 
               
    elif choose =='4':
            print(num1,"+",num2,"=",divide(num1,num2)) 
            
    next=input("Do you want to continue ?(yes/no)")
    if next=="no":
        break
    
else:
    print("Invalid Input")
            
            
            