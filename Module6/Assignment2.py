#validator of float and int added in utility class
from ValidatorUtility import ValidatorUtility
myvalidator = ValidatorUtility()
#class declaration
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description="none"
    #function print_item_cost is for each items cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
    #function print_descriptions is for each descriptions
    def print_descriptions(self):
        print(f"{self.item_name} : {self.item_description}")
#class declaration
class ShoppingCart:
    #constructor
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    #function add_item adding item to cart
    def add_item(self, item):
        self.cart_items.append(item)
    #function remove_item remove item from the cart
    def remove_item(self, item_name):
        item = None
        item= self.getItemByName(item_name)
        if item is None:
            print("Item not found in cart. Nothing removed.")
        else:
            self.cart_items.remove(item)
            print(item_name," removed from cart")
    #function getItemByName get the item from list of items by name
    def getItemByName(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
    #function modify_item get the item from list of items by name and update it
    def modify_item(self, item_name):
        item = None
        item= self.getItemByName(item_name)
        if item is None:
            print("Item not found in cart. Nothing is modified....")
        else:
            item.print_descriptions()
            item.print_item_cost()
            #itemmodify =self.get_itemdetails()
            #item.item_name = itemmodify.item_name
            #item.item_price = itemmodify.item_price
            item.item_quantity =  myvalidator.validate_int("Enter updated Item Quantity:","Invalid input.Please enter Item Quantity:")
            #item.item_description = itemmodify.item_description
            return
    #function get_num_items_in_cart to get items in the cart
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    #function modify_get_cost_of_cart get the cost 
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    #function print_total - printing total
    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Total: ${self.get_cost_of_cart():.2f}")
    #function print_descriptions - printing descriptios
    def print_descriptions(self):
        for item in self.cart_items:
            item.print_descriptions()
    #function print_menu 
    def print_menu(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item Quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
    #function run for looping to get user choice
    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter an option: ")
            if choice == 'a':
                # Add item
                #item = ItemToPurchase()
                print("Add item to cart")
                item =self.get_itemdetails()
                self.add_item(item)
                #item.print_descriptions()
            elif choice == 'r':
                # Remove item
                item_name = input("Enter the name of the item to remove: ")
                self.remove_item(item_name)
            elif choice == 'c':
                # Modify item
                item_to_modify = ItemToPurchase()
                item_name = input("Enter the name of the item to update quantity: ")
                self.modify_item(item_name)
                #item.print_descriptions()
            elif choice == 'i':
                print(f"OUTPUT ITEMS DESCRIPTIONS")
                print(self.customer_name,"'s Shopping Cart - ",self.current_date)
                print(f"Item Descriptions")

                self.print_descriptions()
                #print(f"Total: ${self.get_cost_of_cart():.2f}")
            elif choice == 'o':
                print(f"OUTPUT SHOPPING CART")
                print(self.customer_name,"'s Shopping Cart - ",self.current_date)
                print("Number of Items: ",self.get_num_items_in_cart())
                #self.print_descriptions()
                #print(f"Total: ${self.get_cost_of_cart():.2f}")
                items = self.cart_items
                grandTotal = 0.00
                for item in items:
                    item.print_item_cost()
                    grandTotal +=(item.item_price * item.item_quantity)
                print(f"Total: ${grandTotal:.2f}")
            elif choice == 'q':
                break
            else:
                print("Invalid option. Please try again.")
    #function get_itemdetails get the item details to add
    def get_itemdetails(self):
        #Get item name from users
        name = input("Enter the item name: ")
        #Get item's description from user
        description = input("Enter the item description: ")
        #get price details from user
        price = myvalidator.validate_float("Enter item price: ","Invalid input.Please enter Item price:")
        #Get quantity from user
        qty = myvalidator.validate_int("Enter Item Quantity:","Invalid input.Please enter Item Quantity:")
        item =ItemToPurchase()
        item.item_name = name
        item.item_price =price
        item.item_quantity=qty
        item.item_description=description
        return item

if __name__ == "__main__":
    name = input("Enter the customer's name: ")
    date = input("Enter today's date: ")
    cart = ShoppingCart(name, date)
    cart.run()