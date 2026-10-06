#Question3: Ask the user to enter information for 3 employees:
# Name
# Age
# Salary
#Store each employee's information in a tuple and store all tuples in a list.

emp = []

for i in range(3):
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    salary = int(input("Enter your salary: "))
    print("\n")
    
    employee = (name, age, salary)
    emp.append(employee)

print(emp)