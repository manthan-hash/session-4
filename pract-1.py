import re

def check_password(password):
    if len(password) < 8 or len(password) > 12:
        return "Password must be between 8 and 12 characters long."

    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."

    if not any(char in '!@#$%^&*()_+[]{}|;:,.<>?/~' for char in password):
        return "Password must contain at least one special character."

    return "Password is valid."

user_password = input("Enter your password: ")

result = check_password(user_password)
print(result)
    