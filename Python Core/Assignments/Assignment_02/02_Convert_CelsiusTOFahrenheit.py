# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# converting celcius to Fahrenheit   formula --   (5/9 * c) +32
C = int(input("Enter the temperature in celcius : "))
Fahrenheit = (9/5 * C) + 32
print("After converting Tempertaure in Fahrenheit is : ",Fahrenheit)

# converting fahrenheit to Celcius
F = int(input("Enter the temperature in Fahrenheit : "))
Celcius = 5/9 * (F - 32)
print("After Converting Temp in Celcius : ",Celcius)