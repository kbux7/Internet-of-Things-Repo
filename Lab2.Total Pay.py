#Write a Python program that asks the user to enter the number of hours worked and the hourly rate.
#Calculate the total pay according to the following rules:
#If the employee works 40 hours or less, calculate pay as hours × rate.
#If the employee works more than 40 hours, calculate the first 40 hours at the normal rate and the overtime hours at 1.5 times the hourly rate.
#Display the total pay.

hours_worked: int = int(input("Enter hours worked:  "))
hourly_rate = int(input("Enter hourly rate: "))
extra_hours = hours_worked - 40

if hours_worked <= 40:
    gross_pay = hours_worked * hourly_rate
    print(f'Gross Pay: {gross_pay} Rupees')
elif hours_worked > 40:
    gross_pay = 40 * hourly_rate + extra_hours * (hourly_rate * 1.5)
    print(f"Gross Pay: {gross_pay} Rupees")