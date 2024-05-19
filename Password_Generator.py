import string
import random


def generate_password(length):
    # All possible characters list for the password
    all_characters_list = string.ascii_letters + string.digits + string.punctuation
    # So that the password has at least one lowercase, one uppercase, one digit and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    # Remaining all_characters_list
    password += random.choices(all_characters_list, k=length - 4)
    random.shuffle(password)

    # Join the list to make a string
    return ''.join(password)


def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")

            another = input("Generate another password? (y/n): ").lower()
            if another != 'y':
                break
        except ValueError:
            print("Invalid input! Please enter a numerical value.")


if __name__ == "__main__":
    main()
