# 4. Write a program to enter P, T, R and calculate simple Interest.

Principle = int(input("Enter the Principle : "))
rate = float(input("Enter therate of interset : "))
Time = int(input("Enter thye Duration in Time : "))

Simple_Interset = (Principle * rate * Time ) / 100

Total_amount = Principle + Simple_Interset

print("Simple Interest is : ", Simple_Interset)
print("Total Amount is : ", Total_amount)