# Create a Python script to check the password strength. 

import re

def check_password_strength(password):
    # Check for minimum length of 8 characters
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
    
    return True

def main():
    password = input("Enter a password to check its strength: ")
    
    if check_password_strength(password):
        print("The password is strong.")
    else:
        print("The password is weak. Ensure it is at least 8 characters long, contains both uppercase and lowercase letters, at least one digit, and at least one special character.")

if __name__ == "__main__":
    main()
