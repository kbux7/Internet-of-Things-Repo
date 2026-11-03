#Question 3: write a function using *args to calculate the sum of multiple numbers.

def calculate_sum(*args):
    total = 0

    for num in args:
        total += num

    return total

print(f'Sum: {calculate_sum(10, 20, 30, 40, 50)}')