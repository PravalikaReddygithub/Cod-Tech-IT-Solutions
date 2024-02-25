import string
import random

def generate_password_complexity(length, lowercase, uppercase, numbers):
    
    complexity = {}

    # Validate length
    if length < 6:
        print("Error: Password length must be at least 6 characters.")
        return None

    # Validate at least three character types
    if not any([lowercase, uppercase, numbers]):
        print("Error: Please choose at least three character types.")
        return None

    complexity["length"] = length
    complexity["lowercase"] = lowercase
    complexity["uppercase"] = uppercase
    complexity["numbers"] = numbers
    

    return complexity

def generate_password(complexity):

    chars = []
    if complexity["lowercase"]:
        chars.extend(string.ascii_lowercase)
    if complexity["uppercase"]:
        chars.extend(string.ascii_uppercase)
    if complexity["numbers"]:
        chars.extend(string.digits)
    password = ''.join(random.sample(chars, complexity["length"]))
    return password

def main():
    print("** Secure Password Generator **")
    while True:
        try:
            length = int(input("Enter desired password length (minimum 6): "))
            if length >= 6:
                break
            else:
                print("Invalid input. Please enter a number greater than or equal to 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user choice for character types
    lowercase = input("Include lowercase letters (Y/N): ").upper() == "Y"
    uppercase = input("Include uppercase letters (Y/N): ").upper() == "Y"
    numbers = input("Include numbers (Y/N): ").upper() == "Y"

    # Generate password complexity dictionary
    complexity = generate_password_complexity(length, lowercase, uppercase, numbers)

    # If complexity is valid, generate password
    if complexity:
        password = generate_password(complexity)
        print("\n** Generated Password:")
        print(password)
    else:
        print("Password generation failed due to invalid complexity selection.")

if __name__ == "__main__":
    main()
