---

# Brute Force Password Cracker

This script performs a brute-force attack to crack a password hashed using SHA-256.

## Features

- **Brute Force Attack**: Utilizes a brute-force approach to systematically guess passwords until the correct one is found.
- **Customizable Maximum Length**: Allows customization of the maximum length of the password to search for.
- **Supports Various Character Sets**: Supports ASCII letters, digits, and punctuation characters for password combinations.
- **Efficient Hash Comparison**: Compares hashed password attempts to the target hash value using SHA-256 for efficient and secure comparison.
- **Fast Execution**: Optimized algorithm for fast execution, providing quick results.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/brute-force-password-cracker.git
   ```

2. Navigate to the directory:
   ```bash
   cd brute-force-password-cracker
   ```

3. Run the script:
   ```bash
   python brute_force_password_cracker.py
   ```

4. Enter the hash value of the target password when prompted.

5. The script will attempt to crack the password using a brute-force attack up to a maximum length.

## Example

Suppose you want to crack the password for a hashed value `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8`:

1. Run the script:
   ```bash
   python brute_force_password_cracker.py
   ```

2. Enter the hash value when prompted:
   ```plaintext
   Enter the hash value of the target password: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
   ```

3. The script will attempt to crack the password and provide the result:
   ```plaintext
   Password cracked: password
   Time taken: 0.034691572189331055 seconds
   ```

---
