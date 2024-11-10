#function to capture and validate number of years from the user
def get_years_to_capture_rainfall():
    while True:
        try:
            num_years = int(input("Please enter the number of years to capture: "))
            if num_years < 0:
             print("years cannot be less than 0. Please try again.")
            else:
                break
        except ValueError:
         num_years = print("Invalid input. Please enter valid number of years.")
    return num_years
# function to capture and validate rainfall for month 
def get_rainfall_for_month(month):
    while True:
        try:
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            if rainfall < 0:
                print("Rainfall cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return rainfall
# Initialize variables total rainfall and number of months
num_years = get_years_to_capture_rainfall()  
total_rainfall = 0
total_months = 0
#Static value of months are stored in array
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Outer loop for each year
for year in range(1, num_years + 1):
    print(f"\nYear {year}")
    # Inner loop for each month from months array
    for month in months:
        rainfall = get_rainfall_for_month(month)
        total_months =total_months+1                
        total_rainfall += rainfall
# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months
# Display results
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall inches per month: {average_rainfall:.2f}")
