import collections  
  
list1 = [10, 20, 30, 40, 50, 60]  
list2 = [10, 20, 30, 50, 40, 70]  
list3 = [50, 10, 30, 20, 60, 40]  
  
  
if collections.Counter(list1) == collections.Counter(list2):  
    print("The lists l1 and l2 are the same")  
else:  
    print("The lists l1 and l2 are not the same")  
  
if collections.Counter(list1) == collections.Counter(list3):  
    print("The lists l1 and l3 are the same")  
else:  
    print("The lists l1 and l3 are not the same")  