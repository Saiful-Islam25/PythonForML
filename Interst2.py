
def interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    
    si = (p * t * r)/100
    
    print('The Simple Interest is', si)
    return si
    
interest(3000, 7, 1)
