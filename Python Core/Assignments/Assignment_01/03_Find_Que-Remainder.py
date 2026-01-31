# 3. Program to find quotient and remainder of two numbers.

num1 = int(input("Enter num_1 : "))
num2 = int(input("enter num_2 : "))

if num2 == 0:
    print("Division is not Possible as num2 is zero ")
else :
    Quotient = num1 // num2
    Remainder = num1 % num2

print(f"Quotent is {Quotient} and Remainder is {Remainder}")