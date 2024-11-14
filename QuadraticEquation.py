import math

a=float(input("Enter the value of a : "))
b=float(input("Enter the value of b : "))
c=float(input("Enter the value of c : "))

discriminant=b**2 - 4*a*c

if discriminant>0:
    root1=(-b + math.sqrt(discriminant))/(2*a)
    root2=(-b - math.sqrt(discriminant))/(2*a)
    
    print(f"Root1 is : {root1}")
    print(f"Root2 is : {root2}")

elif discriminant==0:
    root=-b/(2*a)
    print(f"Root is : {root}")
    
else:
    real=-b/(2*a)
    imaginary=math.sqrt(abs(discriminant))/(2*a)
    print(f"Root1 is : {real} + {imaginary}i")
    print(f"Root2 is : {real} - {imaginary}i")




    