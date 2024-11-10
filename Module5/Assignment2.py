#function to capture and validate number of years from the user
def get_months_to_calculate_points():
    while True:
        try:
            num_months = int(input("Please enter the number of months to capture: "))
            if num_months < 0:
             print("months cannot be less than 0. Please try again.")
            else:
                break
        except ValueError:
         num_months = print("Invalid input. Please enter valid number of months.")
    return num_months
# Function to calculate points based on the number of books purchased
def calculate_points_for_Purchase(books_purchased):
    if books_purchased == 0:
        return 0
    elif (books_purchased >1 and books_purchased<4):
        return 5
    elif (books_purchased >3 and books_purchased <6):
        return 15
    elif (books_purchased >5 and books_purchased <8):
        return 30
    elif books_purchased >= 8:
        return 60
    else:
        return 0  
# Get the user input the number of books
def validate_input(month):
    while True:
        try:
            books_purchased = int(input(f"Enter the number of books you purchased for month {month}: "))
            if books_purchased < 0:
                print("Please enter a valid non-negative number of books.")
            else:
        # Call the function to calculate points
                points = calculate_points_for_Purchase(books_purchased)
                print(f"You have earned {points} points for month {month}.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return books_purchased
num_months = get_months_to_calculate_points()  
for month in range(1, num_months + 1):
    print(f"\nMonth {month}")
    books_purchased =validate_input(month)