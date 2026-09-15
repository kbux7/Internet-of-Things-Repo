# 2. Write a Python program that takes hours worked and hourly rate as input from the user,
# then calculates and displays the gross pay.

hours_worked = int(input("Enter hours worked:  "))
hourly_rate = int(input("Enter hourly rate: "))
gross_pay = hours_worked * hourly_rate
print(f'Gross Pay: {gross_pay} Rupees')