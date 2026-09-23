#Question 1: Ask the user for the marks of 5 subjects.
#Calculate:
#•	Total marks
#•	Percentage
#•	Grade
#•	Pass/Fail
#Use a loop to enter the marks.

Total_marks = 0
Result = ''
print("\nEnter your marks for 5 subjects (out of 100)")  
for i in range(0, 5):
    marks = int(input(f"Enter your subject {i+1} marks: "))
    Total_marks += marks
    i += 1
    if marks < 50:
        Result = 'Fail'

print(f'\nTotal Obtained Marks: {Total_marks} Marks')
print(f'Percentage: {Total_marks / 500 * 100:.2f}%')

if Total_marks / 500 * 100 >= 85:
    print("Grade: A+ Grade")
elif Total_marks / 500 * 100 >= 80:
    print("Grade: A Grade")
elif Total_marks / 500 * 100 >= 75:
    print("Grade: B+ Grade")
elif Total_marks / 500 * 100 >= 70:
    print("Grade: B Grade")
elif Total_marks / 500 * 100 >= 65:
    print("Grade: C+ Grade")
elif Total_marks / 500 * 100 >= 60:
    print("Grade: C Grade")
elif Total_marks / 500 * 100 >= 55:
    print("Grade: D+ Grade")
elif Total_marks / 500 * 100 >= 50:
    print("Grade: D Grade")

print(f"Result: {Result}\n")