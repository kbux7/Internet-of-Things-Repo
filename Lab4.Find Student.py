#Question3: Create a list of student names: 
#students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
#Ask the user to enter a student name.
#If the name exists, display:
#Student Found 
#Otherwise: 
#Student Not Found

students = ['Ali', 'Ahmed', 'Sara', 'Ayesha', 'Bilal']
name = str(input("Enter a student name: "))
if name in students:
    print('Student Found')
else:
    print('Student Not Found')