#Question 3: Ask the user to enter 10 numbers.
#Calculate:
#•	Sum
#•	Average
#•	Largest number
#•	Smallest number
#•	Number of even numbers
#•	Number of odd numbers

total = 0
large = 0
small = None
evens = 0
odds = 0

print("\nPlease enter 10 numbers")
for i in range(0, 10):
    num = int(input(f"Enter number {i+1}: "))
    total += num
    if num > large:
        large = num
    if small is None or num < small:
        small = num
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

average = total / 10

print(f"\nSum: {total}")
print(f"Average: {average}")
print(f"Largest number: {large}")
print(f"Smallest number: {small}")
print(f"Number of even numbers: {evens}")
print(f"Number of odd numbers: {odds}\n")