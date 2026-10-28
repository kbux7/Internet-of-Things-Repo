#Question4:Ask the user for a number and check whether it exists in the set {10, 20, 30, 40, 50}. 

num_set = {10, 20, 30, 40, 50}
user_number = int(input("Enter a number: "))
if user_number in num_set:
    print(f"The number {user_number} exists in the set.")
else:
    print(f"The number {user_number} does not exist in the set.")