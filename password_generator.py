"""
Task 01: Strong Password Generator
Internship Project

Description:
A secure, interactive command-line password generator written in Python.
Uses Python's built-in `secrets` and `string` modules to generate cryptographically
strong random passwords containing uppercase letters, lowercase letters, numbers,
and symbols.
"""

import string
import secrets


def generate_password(length: int) -> str:
    """
    Generates a cryptographically secure random password of specified length.

    Ensures that the generated password contains at least:
    - 1 Uppercase letter
    - 1 Lowercase letter
    - 1 Digit
    - 1 Special symbol

    Args:
        length (int): Desired length of the password (minimum 4).

    Returns:
        str: Generated strong random password.
    """
    # Define character sets using standard library 'string' module
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    # Combined pool of all allowed characters
    all_chars = uppercase_chars + lowercase_chars + digit_chars + symbol_chars

    # Guarantee at least one character from each core category
    guaranteed_chars = [
        secrets.choice(uppercase_chars),
        secrets.choice(lowercase_chars),
        secrets.choice(digit_chars),
        secrets.choice(symbol_chars),
    ]

    # Fill the remaining length with random choices from the combined pool
    remaining_length = length - len(guaranteed_chars)
    random_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Combine all characters
    password_list = guaranteed_chars + random_chars

    # Securely shuffle the password list using SystemRandom
    secrets.SystemRandom().shuffle(password_list)

    # Convert list back into a single string
    return "".join(password_list)


def get_password_length() -> int:
    """
    Prompts the user to enter the desired password length and validates the input.

    Returns:
        int: Validated password length (>= 4).
    """
    min_length = 4

    while True:
        user_input = input(f"Enter desired password length (minimum {min_length}): ").strip()

        # Check if input is a valid integer
        try:
            length = int(user_input)
            if length < min_length:
                print(f"[!] Invalid length: Password must be at least {min_length} characters long. Please try again.\n")
                continue
            return length
        except ValueError:
            print("[!] Invalid input: Please enter a valid positive number.\n")


def print_banner():
    """Displays a clean and professional welcome header."""
    print("=" * 60)
    print("              SECURE PASSWORD GENERATOR              ")
    print("=" * 60)
    print("Generate strong, cryptographically secure passwords easily.")
    print("-" * 60)


def main():
    """Main function to run the password generator application loop."""
    print_banner()

    while True:
        # Step 1: Get valid password length from user
        length = get_password_length()

        # Step 2: Generate the password
        password = generate_password(length)

        # Step 3: Display results
        print("\n" + "-" * 60)
        print("Generated Password:")
        print(f"  >>> {password} <<<")
        print("-" * 60)

        # Step 4: Ask user if they want to generate another password
        while True:
            repeat = input("\nDo you want to generate another password? (y/n): ").strip().lower()
            if repeat in ["y", "yes"]:
                print("\n" + "=" * 60 + "\n")
                break
            elif repeat in ["n", "no"]:
                print("\nThank you for using Secure Password Generator. Stay safe!\n")
                return
            else:
                print("[!] Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
