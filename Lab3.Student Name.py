#Question 2: Take a student's name and display:
#•	Name in uppercase
#•	Name in lowercase
#•	Number of characters
#•	First character
#•	Last character

StudentName = str(input("Enter Student Name: "))
print(f"\nStudent Name: {StudentName.upper()}")
print(f"Student Name: {StudentName.lower()}")
print(f"Student Name: {len(StudentName)}")
print(f"Student Name: {StudentName[0]}")
print(f"Student Name: {StudentName[-1]}")