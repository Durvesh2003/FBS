# Find the area and circumference of circle.
import math 

r = int(input("Enter the radius of circle : "))

area = math.pi * r * r

circumference = 2 * math.pi * r

print(f"Area of Circle is {area} and Circumference is {circumference}")