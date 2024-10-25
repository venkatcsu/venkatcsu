# Enter the meal price
meal_charge = float(input("Enter the Price for the meal: "))
# Calculate sales tax (7%) on meal price
sales_tax = meal_charge * (7/100)
# Calculate tip (18%) on meal price
tip = meal_charge * (18/100)
# Calculate total amount
total_amount = meal_charge + sales_tax + tip
# Display the results
print(f"\nMeal Price: ${meal_charge:.2f}")
print(f"Sales tax (7%): ${sales_tax:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Total amount: ${total_amount:.2f}")

