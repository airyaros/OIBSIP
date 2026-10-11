# Secure Password Generator
import random
import string

def generate_password():
    print("--- Secure Password Generator ---")
    
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters for security.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print("Choose complexity level:")
    print("1. Letters & Numbers (Basic)")
    print("2. Letters, Numbers & Symbols (Secure)")
    
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        characters = string.ascii_letters + string.digits
    elif choice == '2':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice. Defaulting to secure (Letters, Numbers & Symbols).")
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated Password: {password}\n")

if __name__ == "__main__":
    generate_password()
