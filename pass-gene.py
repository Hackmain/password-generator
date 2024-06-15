import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a 12-character long password
print(generate_password(12))
print("follow us in the instagram esefkh740_ & cyberhex.tech_")
