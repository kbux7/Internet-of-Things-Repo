#Question 5: create a function that checks whether a password:
# Contains at least 8 characters.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit.
# Contains at least one special character.

def check_pass(password):

    if len(password) < 8:
        return "Password must contain at least 8 characters."

    if not any(char.isupper() for char in password):
        return "Password must contain an uppercase letter."

    if not any(char.islower() for char in password):
        return "Password must contain a lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Password must contain a digit."

    if not any(not char.isalnum() for char in password):
        return "Password must contain a special character."

    return "its valid one!"


password = input("Enter your password: ")

print(check_pass(password))