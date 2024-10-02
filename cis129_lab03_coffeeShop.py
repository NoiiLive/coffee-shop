# cis129_lab03_coffeeShop.py
# Author: Elle Green
# Date: 2024-10-01
# Coffee Shop Simulator that calculates a receipt based on user input for coffee and muffin orders.

# Define the prices
coffee_price = 5
muffin_price = 4
tax_rate = 0.06

# Get user input for the number of coffees and muffins
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))

# Calculate subtotal
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal = subtotal_coffee + subtotal_muffin

# Calculate tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Display the receipt
print("\n" + "*" * 39)
print("My Coffee and Muffin Shop")
print(f"{num_coffees} Coffee at ${coffee_price} each: $ {subtotal_coffee:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: $ {subtotal_muffin:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("*" * 39)
