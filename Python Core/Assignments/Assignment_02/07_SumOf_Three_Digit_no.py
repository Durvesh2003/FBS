# 7. Find the sum of three-digit number.
num = int(input("Enter the Three Digit number : "))   # suppose 135

r1 = num % 10             # 5 as remainder
num = num // 10           # 13
r2 = num % 10             # 3 as a remainder
num = num // 10           # 1
r3 = num % 10             # 1 as a remainder
num = num // 10           # 0

sum = r1 + r2 + r3 

print("Sum of three diit number is : ",sum)