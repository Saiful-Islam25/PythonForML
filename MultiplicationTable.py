num=int(input("Enter a number : "))

print("The multiplication table of the given number is ")
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")