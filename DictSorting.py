daynames = { 'one' : 'Monday' ,  'six' : 'Saturday' ,'three' : 'Wednesday' ,  'two' : 'Tuesday' , 'five': 'Friday' ,  'seven': 'Sunday' }  
print(daynames)  

number = { 'one' : 1 , 'two' : 2 , 'three' : 3 , 'four' : 4 , 'five' : 5 , 'six' : 6 , 'seven' : 7}  
print(sorted(daynames , key=number.__getitem__))  
print([daynames[i] for i in sorted(daynames , key=number.__getitem__)])  