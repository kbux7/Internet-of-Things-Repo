#Write a Python program to create an advanced student marksheet. The program should:
#Ask the user to enter the student's name and roll number.
#Input marks for 5 subjects.
#Calculate the total marks and percentage.
#Determine the grade according to:
#80–100% → A+
#70–79% → A
#60–69% → B
#50–59% → C
#40–49% → D
#Below 40% → F
#Check whether the student passed or failed.
#If the student scores below 40 in any subject, declare the student a Fail regardless of the overall percentage.
#Display a complete marksheet containing the student's information, such as name and roll no., subject marks, total, percentage, grade, and result.


Student_Name = str(input("Enter Student Name: "))
Roll_No = int(input("Enter Student Roll No: "))

Sub1_Marks = int(input("\nEnter Subject 01 Marks: "))
Sub2_Marks = int(input("Enter Subject 02 Marks: "))
Sub3_Marks = int(input("Enter Subject 03 Marks: "))
Sub4_Marks = int(input("Enter Subject 04 Marks: "))
Sub5_Marks = int(input("Enter Subject 05 Marks: "))

Obtained_Marks = Sub1_Marks + Sub2_Marks + Sub3_Marks + Sub4_Marks + Sub5_Marks
Total_Marks = 100 + 100 + 100 + 100 + 100
Percentage = float(Obtained_Marks / Total_Marks * 100)

print("\n-----Student_Marksheet-----\n")
print("Student Name: ", Student_Name)
print("Student Roll No: ", Roll_No)
print("\nSubject 01 Marks: ", Sub1_Marks, "\nSubject 02 Marks: ", Sub2_Marks, "\nSubject 03 Marks: ", Sub3_Marks, "\nSubject 04 Marks: ", Sub4_Marks, "\nSubject 05 Marks: ", Sub5_Marks)
print("\nTotal Obtained Marks: ", Obtained_Marks)
print(f"Percentage: {Percentage:.2f} %")

if Percentage >= 80:
    print("Grade: A+")
elif Percentage >= 70:
    print("Grade: A")
elif Percentage >= 60:
    print("Grade: B")
elif Percentage >= 50:
    print("Grade: C")
elif Percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")

if Sub1_Marks < 40 or Sub2_Marks < 40 or Sub3_Marks < 40 or Sub4_Marks < 40 or Sub5_Marks < 40:
    print("Result: Fail")
else:
    print("Result: Pass")