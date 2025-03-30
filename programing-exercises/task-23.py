import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=6))

def save_passwords_to_file(filename, count=1000):
    with open(filename, "w") as file:
        for _ in range(count):
            file.write(generate_password() + "\n")

save_passwords_to_file("passwords.txt")

print("Wygenerowano 1000 losowych haseł i zapisano do passwords.txt")