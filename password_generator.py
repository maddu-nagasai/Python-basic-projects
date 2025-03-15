import random
import string
import pyperclip  # To copy the password to clipboard

def generate_password(length, use_uppercase, use_numbers, use_special):
    """Generate a strong password based on user preferences."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if length < 4:
        return "Error: Password length must be at least 4 characters."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n🔒 Password Generator 🔒")
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    if "Error" not in password:
        print(f"\nGenerated Password: {password}")
        pyperclip.copy(password)
        print("Password copied to clipboard! ✅")
    else:
        print(password)

if __name__ == "__main__":
    main()
