import itertools
import string
import time
import hashlib

def brute_force_password(target_hash, max_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    start_time = time.time()

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            attempt = ''.join(combination)
            hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()
            if hashed_attempt == target_hash:
                end_time = time.time()
                return attempt, end_time - start_time

def main():
    target_hash = input("Enter the hash value of the target password: ")
    max_length = 8

    cracked_password, time_taken = brute_force_password(target_hash, max_length)
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
        print(f"Time taken: {time_taken} seconds")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
