    
lst = ["Python", "Remove", "Elements", "List", "Tutorial", "Clear", "Pop", "Remove", "Delete"]    
print("The Initial list is ", lst)    
    
del lst[0]    
print("After removing the first element new list is", lst)    
    
del lst[-1]    
print("After removing the last element new list is", lst)    
    
del lst[:3]    
print("After removing element from index:", lst)    
    
del lst[-2]    
print("After removing the last 2 elements from the list", lst)    
    
del lst[1:7]    
print("After removing elements present in the range 1:7", lst) 


my_list = [1, 2, 3, 4, 5]  
my_list.discard(3)   
print(my_list)    