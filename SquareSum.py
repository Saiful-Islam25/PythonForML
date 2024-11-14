def square_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
        
    return sum

n=int(input("Enter the value of n : "))
print(f"The square sum of n natural numbers is : ",square_sum(n))