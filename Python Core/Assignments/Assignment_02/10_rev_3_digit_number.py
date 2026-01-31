# 10. Write a program to reverse three-digit number.
num = int(input("enter the three digit number : "))   # Suppose 345

r1 = num % 10                  # 5
num = num // 10                # 34
r2 = num % 10                  # 4
num = num// 10                 # 3
r3 = num % 10                  # 3
num = num // 10                # 0

rev = (r1*100) + (r2 * 10) + r3

print("Reverse is : ",rev)
