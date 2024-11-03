# Class declaration
class ItemToPurchase:
#The default constructor __init__ initializes these attributes to "none", 0.0, and 0, respectively. 
	def __init__(self, item_name="none", item_price=0.0, item_quantity=0): 
		self.item_name = item_name 
		self.item_price = item_price 
		self.item_quantity = item_quantity
#The method accepts item object as parameter and calculate total cost and print.
	def print_item_cost(self):
		total_cost = self.item_price * self.item_quantity 
		print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
#Step 1 Example assinging item values and  print
item1 = ItemToPurchase("Bottled Water", 1.0, 10) 
print("Example of print_item_cost() output:")
item1.print_item_cost()
#Step 2 items from user input and call contructor and call print_item_cost() to calculate and print
items = []
#variable to store number of items in cart(2 items hardcoded in variable)
k=2
for i in range(k):
	if i==0:
		print("Item "+str(i+1))
	else:
		print("\nItem "+str(i+1))
	name = input("Enter the item name:\n")
	price = float(input("Enter the item price:\n"))
	qty = int(input("Enter the item quantity:\n"))
	itemObj = ItemToPurchase(name,price,qty)
	itemObj.print_item_cost()
	items.append(itemObj)
print("\nITOTAL COST")
#Step 3 Step 3: Add the costs of the items together and output the total cost.
grandTotal =0.0
for item in items:
	item.print_item_cost()
	grandTotal+=(item.item_price * item.item_quantity)
print(f"Total: ${grandTotal:.2f}")