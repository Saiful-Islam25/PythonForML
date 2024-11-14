def happy_num(num):
    rem=0
    sum=0
    
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10 
    return sum

print("List of happy numbers between 1 and 100 :")
        
for i in range(1,101):
    res=i
    
    while(res!=1 and res !=4):
        res=happy_num(res)
        
    if (res==1):
        print(i),
        #print(" ")