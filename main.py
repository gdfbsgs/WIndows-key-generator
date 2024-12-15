print("hello wotld")
import random
import string

def generate_windows_key():
    key_parts = []
    for _ in range(5):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        key_parts.append(part)
    return '-'.join(key_parts)

if __name__ == "__main__":
    for _ in range(100):  # Generate 5 keys
        print(generate_windows_key())