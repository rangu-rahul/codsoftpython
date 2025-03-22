import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter password length (default is 12): ") or 12)
    if length < 4:
        print("Password length should be at least 4 for security.")
    else:
        print(f"Generated Password: {generate_password(length)}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

