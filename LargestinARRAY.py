def largest(arr):
    if not arr:
        return "Array is empty"
    
    largest=arr[0]
    
    for element in arr:
        if element>largest:
            largest=element
            
    return largest

#array=[2,5,9,75,83,47,23]
array=int(input("Enter the values of the array : "))
result=largest(array)
print(f"The largest element in the array is : {result}")
    