print('Case:1************************')
# Create an array to store daily temperatures for 7 days
daily_temps_forweek = [0] * 7
# Record temperatures for each day of week
for day in range(1, 8):
    temp = float(input("Enter the high temperature for day {day}: "))
    # storing in array
    daily_temps_forweek[day - 1] = temp
for i in range(0,len(daily_temps_forweek)):
    # printing daily temperature stored in array.
    print('Day',i+1,daily_temps_forweek[i])
# average temperature of the week.
avg_temp = sum(daily_temps_forweek)/len(daily_temps_forweek)
print('Average temperature for the week:{:.2f}'.format(avg_temp))
print('\n')
print('Case:2************************')
# Create an array to store student grades
student_grades = [78, 95, 82, 90, 100]
#Find minimum value in the array
min_grade = min(student_grades)
#Find maximum value in the array
max_grade = max(student_grades)
print('Minimum garde :',min_grade)
print('Maximum garde :',max_grade)
print('\n')
print('Case:3************************')
# Create an array to store products and quantity
products = [
    {"name": "iphone", "quantity": 30},
    {"name": "samsung", "quantity": 25},
    {"name": "pixel", "quantity": 20}
]
print('Before sorting:',products)
#Sorting on quantity using lambda 
products.sort(key=lambda x: x["quantity"])
print('After sorting on QTY',products)
#Sorting on name using lambda 
products.sort(key=lambda x: x["name"])
print('After sorting on Name',products)
