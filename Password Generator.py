import random
import string

def generate_password(length):
    # Define character sets: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input: Get password length
try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password length should be at least 4 for better security.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
