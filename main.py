import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."

    # Check for special characters
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets the criteria for strength."

def main():
    # Prompt user for a password
    password = input("Enter the password to check its strength: ")

    # Check password strength
    result = check_password_strength(password)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()

