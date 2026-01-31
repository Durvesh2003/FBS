# 3. Convert distant given in feet and inches into meter and centimeter.
# 1 foot = 30.48 cm
# 1 inch = 2.54 cm
# 1 meter = 100 cm

feet = int(input("Enter Feet : "))
inches = int(input("Enter Inces : "))

Total_centimeters = feet * 30.48 + inches * 2.54
centimeters = Total_centimeters % 100
meters = float(Total_centimeters // 100)

print (F" Centimeters : {centimeters} cm")
print (f"Meters : {meters} m")