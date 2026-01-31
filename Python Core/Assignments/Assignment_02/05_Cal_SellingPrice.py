# 5. WAP to calculate selling price of book based on cost price and discount.
price = int(input("Enter the price of Product : "))
Discount = int(input("Enter the Discount(Between 5% to 20%^) : "))

selling_Price =price - (price * (Discount/100))

print("Total Selling Price after the discount is : ",selling_Price)