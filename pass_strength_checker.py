# Q.1 Create a Python script to check the password strength. 

import re

def check_password_strength(password):
    # Check the minimum length
    if len(password) < 8:
        return False

    # Check for both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all criteria are met, return True
    return True

def main():
    # Prompt user for password input
    password = input("Enter a password to check its strength: ")

    # Check the strength of the password
    if check_password_strength(password):
        print("Your password is strong.")
    else:
        print("Your password is weak. It must be at least 8 characters long, contain both uppercase and lowercase letters, at least one digit, and at least one special character.")

if __name__ == "__main__":
    main()