def convert_to_24_hour_format(time_input): 
    # Check if the input is in 12-hour format (with AM/PM)
    if 'AM' in time_input or 'PM' in time_input:
        # Remove the AM/PM and split the time
        time_parts = time_input[:-2].strip().split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        
        # Convert to 24-hour format
        if 'PM' in time_input and hours != 12:
            hours += 12
        elif 'AM' in time_input and hours == 12:
            hours = 0
    
    else:
        # Assume input is in 24-hour format
        time_parts = time_input.split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])

        # Validate the input for 24-hour format
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            print("Invalid time input in 24-hour format.")
            return
    # Validate hours and minutes after conversion
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        print("Invalid time input.")
        return
    # Return the 24 hour forramtted 
    return f"{hours:02}:{minutes:02}"
#User input to get current time
time_input = input("Enter the current time (e.g., 2:30 PM or 14:30): ").strip()
# Call the function to convert current time to 24hr format
converted_time_24hr = convert_to_24_hour_format(time_input)
try:
    #split into hours and minutes
    hours, minutes = map(int, converted_time_24hr.split(':'))
except ValueError:
    print("Invalid time format.")
 # User input to Get the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
#convert hours to minutes
total_minutes = (hours * 60) + minutes + (hours_to_wait * 60)
# Calculate the time when the alarm goes off
alarm_hour = total_minutes // 60 % 24
alarm_minute = total_minutes % 60
alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}"
# Display the result
print(f"The alarm will go off at {alarm_time}")

