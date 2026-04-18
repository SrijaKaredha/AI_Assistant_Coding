'''Task 1 – Input Validation Check
Task:
Analyze an AI-generated Python login script for input validation
vulnerabilities.
Instructions:
* Prompt AI to generate a simple username-password
login program.
* Review whether input sanitization and validation are
implemented.
* Suggest secure improvements (e.g., using re for input
validation).
Expected Output:
* A secure version of the login script with proper input
validation.'''

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# Improved version with input validation
import re
import getpass

def validate_username(username):
    # Only letters and numbers, 3–15 characters
    return re.fullmatch(r"[A-Za-z0-9]{3,15}", username)

def validate_password(password):
    # At least 6 chars, 1 letter + 1 number
    return re.fullmatch(r"(?=.[A-Za-z])(?=.\d)[A-Za-z\d]{6,}", password)

def login():
    username = input("Enter username: ").strip()
    
    if not validate_username(username):
        print("Invalid username format!")
        return

    password = getpass.getpass("Enter password: ")

    if not validate_password(password):
        print("Invalid password format!")
        return

    # Dummy stored credentials
    if username == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Credentials")

login()

#Task 2
'''Task 2 – SQL Injection Prevention
print(loaded_data)
