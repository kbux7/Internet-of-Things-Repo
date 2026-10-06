#Question4: Given:
#numbers = (10, 15, 20, 25, 30, 35, 40)
#Use a loop to count:
# Even numbers
# Odd numbers

number = (10, 15, 20, 25, 30, 35, 40)
even = 0
odd = 0
for i in number:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1    

print(f'There are {even} even and {odd} odd numbers')       