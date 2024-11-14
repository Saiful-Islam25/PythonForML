import random  
import string  
def specific_string(length):  
    sample_string = 'pqrstuvwxy' 
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  
  
specific_string(8)   
specific_string(10)  