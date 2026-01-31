# 5. Write a program to enter P, T, R and calculate Compound Interest.
Principle = int(input("Enter the Principle : "))
rate = float(input("Enter therate of interset : "))
Time = int(input("Enter thye Duration in Time : "))

Fianl_amount = int(Principle* ( 1 + (rate/100)) ** Time)

Compound_Interest = Fianl_amount - Principle

print("Final_amount is : ",Fianl_amount)
print("Compound_Interest is : ",Compound_Interest)