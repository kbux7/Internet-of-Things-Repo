#Question 5: Ask the user for a number n and print multiplication tables from 1 to n.

n = int(input("\nEnter a number to generate its table: "))
print(f"\nTable of {n}")
for i in range(1, 13):
    print(f'{n} x {i} = {n*i}')
print("\n")