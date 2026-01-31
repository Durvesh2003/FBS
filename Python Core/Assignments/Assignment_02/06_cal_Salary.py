# 6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

Basic = int(input("Enter the Basic Salary : "))

da = 0.10 * Basic   # Dearness Allowance
ta = 0.12 * Basic   # Travelling Allowance
hra = 0.15 * Basic  # House Rent Allowance

Total_salary = Basic + da + ta + hra
print (f"da : {da} \n ta : {ta} \n hra : {hra} \n Total salary : {Total_salary}")
