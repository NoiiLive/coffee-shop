# cis129_lab03_coffeeShop.py
# Author: Elle Green
# Date: 2024-10-01
# Coffee Shop Simulator that calculates a receipt based on user input for coffee and muffin orders.

# Define the prices
coffee_price = 5
muffin_price = 4
donut_price = 4
bagel_price = 5

# Tax rate
tax_rate = 0.06

# Get user input for the number of coffees and muffins
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_donuts = int(input("Number of donuts bought? "))
num_bagels = int(input("Number of bagels bought? "))

# Calculate subtotals
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal_donut = num_donuts * donut_price
subtotal_bagel = num_bagels * bagel_price

subtotal = subtotal_coffee + subtotal_muffin + subtotal_donut + subtotal_bagel

# Calculate tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Display the receipt
print("\n" + "*" * 39)
print("Elle's Coffee Shop")
print(f"{num_coffees} Coffee at ${coffee_price} each: $ {subtotal_coffee:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: $ {subtotal_muffin:.2f}")
print(f"{num_donuts} Donuts at ${donut_price} each: $ {subtotal_donut:.2f}")
print(f"{num_bagels} Bagels at ${bagel_price} each: $ {subtotal_bagel:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("*" * 39)
