# 7. Program to Find the Roots of a Quadratic Equation

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate Discriminant d
d = b**b - (4*a*c)

if d > 0 :
    root1 = (-b + d**0.5) / 2* a           # d**0.5 means root of d
    root2 = (-b - d**0.5) / 2* a
    print( f" both roots are real and they are {root1} and {root2} " )
elif  d == 0 :
    root = -b / 2 * a
    print("Both roots are same and root is : ",root)

else :
    print("Roots are not possible/real ")
