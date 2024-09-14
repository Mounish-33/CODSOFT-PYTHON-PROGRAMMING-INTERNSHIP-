import random
import string

def generate_password(length):
    # Combine all the possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Prompt the user for the desired password length
    length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password: " + password)

if __name__ == "__main__":
    main()
