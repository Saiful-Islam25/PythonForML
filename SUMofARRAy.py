def sum_array(arr):
    total=0
    
    for element in arr:
        total+=element   
    return total


a=[1,2,3,4,5,6,7]
result=sum_array(a)
print("Sum of the array : ",result)