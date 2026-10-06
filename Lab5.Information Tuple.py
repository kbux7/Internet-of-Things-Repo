#Question1: Ask the user for:
# Name
# Age
# Program
# Marks
#Store the information in a tuple.

name = str(input('Enter your name: '))
age = int(input('Enter your age: '))
program = str(input('Enter your program: '))
marks = int(input ('Enter your marks: '))

infotuple = (name, age, program, marks)
print(infotuple)
