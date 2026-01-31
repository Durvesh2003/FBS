# 8. Write a program to convert days into years, weeks and days.
days = int(input("Enter the number of days : "))

years = days // 365
remaining_days = days % 365

weeks = days // 7
days_left = remaining_days % 7

print("Years : ", years)
print("Weeks : ", weeks)
print("Days : ", days_left)