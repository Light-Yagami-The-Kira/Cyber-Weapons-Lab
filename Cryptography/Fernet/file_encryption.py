from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(input_file, output_file, key):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file, 'wb') as f_out:
        f_out.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f_in:
        encrypted_data = f_in.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, 'wb') as f_out:
        f_out.write(decrypted_data)

# Generate a key
key = generate_key()

# File paths
input_file = 'screen_record.avi'
encrypted_file = 'encrypted_file2.txt'
decrypted_file = 'decrypted_file.avi'

# Encrypt the file
encrypt_file(input_file, encrypted_file, key)
print(f"File '{input_file}' encrypted and saved as '{encrypted_file}'.")

# Decrypt the file
decrypt_file(encrypted_file, decrypted_file, key)
print(f"File '{encrypted_file}' decrypted and saved as '{decrypted_file}'.")
