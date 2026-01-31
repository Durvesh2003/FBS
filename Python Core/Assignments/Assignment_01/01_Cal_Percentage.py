# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects

Maths = int(input("Enter the marks of Maths : "))
English = int(input("Enter the marks of English : "))
Science = int(input("Enter the marks of Science : "))
CS = int(input("Enter the marks of CS : "))
Hindi = int(input("Enter the marks of Hindi : "))

percentage = (Maths + English + Science + CS + Hindi) / 5

print("Total percentage of student is : ",percentage)