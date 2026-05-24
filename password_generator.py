import random
import string

def generate_password(length):
    """
    Generate a strong random password of specified length.
    
    The password includes:
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Digits (0-9)
    - Special characters (!@#$%^&*)
    
    Args:
        length (int): The desired length of the password
        
    Returns:
        str: The generated password
    """
    # Define character sets for password generation
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    # Combine all character sets
    all_chars = uppercase + lowercase + digits + special_chars
    
    # Ensure password includes at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password with random characters from all sets
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password to randomize character positions
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)


def main():
    """Main function to run the password generator application."""
    print("=" * 50)
    print("       PASSWORD GENERATOR APPLICATION")
    print("=" * 50)
    print()
    
    while True:
        try:
            # Prompt user for password length
            length = input("Enter the desired password length (minimum 4): ")
            
            # Convert input to integer
            length = int(length)
            
            # Validate input
            if length < 4:
                print("Error: Password length must be at least 4 characters.")
                print()
                continue
            
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print()
            print("-" * 50)
            print(f"Generated Password: {password}")
            print("-" * 50)
            print()
            
            # Ask if user wants to generate another password
            another = input("Generate another password? (yes/no): ").lower()
            if another not in ['yes', 'y']:
                print("\nThank you for using Password Generator!")
                break
            print()
            
        except ValueError:
            print("Error: Please enter a valid integer for the password length.")
            print()


if __name__ == "__main__":
    main()
