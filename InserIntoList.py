list=[10,20,30,40,50,60]
print("Current elements in the list are :",list )

insertion=list.insert(4,67)
print("The new list is : ",list)

n=int(input("Enter a number to add the list : "))
index=int(input("Enter the index to add the number : "))

list.insert(index,n)
print('Updated Numbers List:', list)  
