# IncodeVision Python Internship
## Task 01: Strong Password Generator

An interactive, cryptographically secure command-line Password Generator developed in Python for the **IncodeVision Python Internship**. This application generates robust, randomized passwords with a balanced mixture of uppercase letters, lowercase letters, numbers, and special symbols.

---

## 📌 Project Overview

In the modern digital landscape, utilizing strong and resilient passwords is a critical first line of defense against unauthorized access. This project fulfills **Task 01** of the IncodeVision Python Internship by providing an easy-to-use, secure tool designed to generate high-entropy passwords tailored to custom user-specified lengths while guaranteeing strict complexity criteria.

---

## ✨ Features

- **🔒 Cryptographically Secure Randomness**:
  - Utilizes Python's standard `secrets` module (CSPRNG) for true hardware/OS-level entropy rather than pseudo-random number generators (`random`).
- **🛡️ Guaranteed Complexity**:
  - Every password generated contains a guaranteed mix of:
    - At least 1 Uppercase letter (`A-Z`)
    - At least 1 Lowercase letter (`a-z`)
    - At least 1 Number (`0-9`)
    - At least 1 Special Symbol (`!@#$%^&*()-_=+[]{}|;:,.<>?`)
- **📏 Customizable Length**:
  - Allows users to specify any desired length (minimum length enforced: 4).
- **🔀 Secure In-Place Shuffling**:
  - Uses `secrets.SystemRandom().shuffle()` to eliminate predictable placement patterns.
- **⚡ Robust Input Validation**:
  - Safely handles non-integer inputs, negative numbers, and lengths below minimum with descriptive error feedback.
- **🔁 Interactive Multi-Run Session**:
  - Users can generate multiple passwords consecutively without restarting the program.
- **📦 Zero External Dependencies**:
  - Built strictly with Python's Standard Library.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3.8+
- **Standard Library Modules**:
  - `secrets`: Cryptographic random number generation and secure shuffling.
  - `string`: Predefined constants for character sets (letters, digits, symbols).

---

## 🚀 How to Run the Project

### 1. Prerequisites
Ensure Python 3 is installed on your system. You can verify your Python version by running:
```bash
python --version
```

### 2. Clone / Navigate to the Repository
```bash
git clone https://github.com/nihitchoudhary690-sys/Incodevision_Python_Internship.git
cd Incodevision_Python_Internship
```
*(Or navigate into the project directory if working locally)*:
```bash
cd Task_01_Password_Generator
```

### 3. Run the Script
```bash
python password_generator.py
```

### 4. Interactive Usage
- Enter your desired password length when prompted (e.g., `12`).
- Copy your generated password from the terminal.
- Enter `y` to generate another password or `n` to exit.

---

## 📷 Sample Terminal Output

```text
============================================================
              SECURE PASSWORD GENERATOR              
============================================================
Generate strong, cryptographically secure passwords easily.
------------------------------------------------------------
Enter desired password length (minimum 4): 14

------------------------------------------------------------
Generated Password:
  >>> K#9xP2!mQv8$Z1 <<<
------------------------------------------------------------

Do you want to generate another password? (y/n): n

Thank you for using Secure Password Generator. Stay safe!
```

---

## 📂 Project Structure

```text
Task_01_Password_Generator/
├── password_generator.py   # Core Python script with generator logic
├── README.md               # Project documentation and guide
└── .gitignore              # Ignores bytecode, caches, and environment files
```

---

## 🏢 Internship & Company Information

- **Company / Organization**: IncodeVision
- **Role / Track**: Python Development Intern
- **Task**: Task 01 – Strong Password Generator
- **Developer**: Nihit Choudhary
- **Repository**: [Incodevision_Python_Internship](https://github.com/nihitchoudhary690-sys/Incodevision_Python_Internship.git)
