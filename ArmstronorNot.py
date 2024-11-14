num= int(input("Enter a number : "))

num_str=str(num)
num_dig=len(num_str)

sum_powers=0
temp=num

while temp>0:
    digit=temp%10
    sum_powers+=digit**num_dig
    temp//=10
    
    
if sum_powers==num:
    print(f"{num} is an armstrong number.")
    
else:
    print(f"{num} is not an armstrong number.")