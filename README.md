# Task 01: Secure Password Generator

A strong, interactive command-line Password Generator developed in Python. This project generates cryptographically secure, customizable random passwords containing a balanced mixture of uppercase letters, lowercase letters, digits, and special characters.

---

## 📌 Project Overview

In today's digital era, using weak or easily guessable passwords poses a major security threat. This project provides a simple yet highly secure tool that creates resilient passwords meeting standard complexity requirements.

---

## ✨ Features

- **Cryptographically Secure**: Implements Python's built-in `secrets` module (using system-level entropy / `CSPRNG`) rather than standard pseudo-random number generators (`random`).
- **Guaranteed Complexity**: Every generated password is guaranteed to contain at least:
  - 1 Uppercase letter (`A-Z`)
  - 1 Lowercase letter (`a-z`)
  - 1 Digit (`0-9`)
  - 1 Special symbol (`!@#$%^&*...`)
- **Customizable Length**: Accepts any password length of 4 characters or greater.
- **True Cryptographic Shuffling**: Uses `secrets.SystemRandom().shuffle()` to eliminate character placement bias.
- **Robust Input Validation**: Gracefully handles non-numeric values, negative numbers, and lengths below the minimum threshold with friendly error messages.
- **Interactive Multi-Run Loop**: Allows generating multiple passwords in a single session without restarting the script.
- **Zero External Dependencies**: Pure Python implementation using only the Python Standard Library.

---

## 🛠️ Technologies Used

- **Language**: Python 3.8+
- **Standard Library Modules**:
  - `secrets`: For cryptographically secure random numbers and character selection.
  - `string`: For clean constants representing character sets.

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have Python 3 installed on your machine. You can verify this by running:
```bash
python --version
```

### Steps to Run

1. **Navigate to the Project Directory**:
   ```bash
   cd Task_01_Password_Generator
   ```

2. **Run the Script**:
   ```bash
   python password_generator.py
   ```

3. **Follow the On-Screen Prompts**:
   - Enter your desired password length (minimum 4).
   - Copy the generated password.
   - Choose `y` to generate another password or `n` to exit.

---

## 📷 Sample Output

```text
============================================================
              SECURE PASSWORD GENERATOR              
============================================================
Generate strong, cryptographically secure passwords easily.
------------------------------------------------------------
Enter desired password length (minimum 4): 12

------------------------------------------------------------
Generated Password:
  >>> K#9xP2!mQv8$ <<<
------------------------------------------------------------

Do you want to generate another password? (y/n): n

Thank you for using Secure Password Generator. Stay safe!
```

---

## 📂 Project Structure

```text
Task_01_Password_Generator/
├── password_generator.py   # Main Python script
└── README.md               # Project documentation
```

---

## 👤 Author
- **Internship Task 01** - Python Programming
