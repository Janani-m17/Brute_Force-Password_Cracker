# Brute Force Password Cracker

This script performs a brute-force attack to crack a password hashed using SHA-256.

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

5. The script will attempt to crack the password using a brute-force attack up to a maximum length of 8 characters.

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
