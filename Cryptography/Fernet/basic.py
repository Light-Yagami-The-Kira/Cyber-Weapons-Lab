from cryptography.fernet import Fernet

# GENERATE A KEY
key = Fernet.generate_key()
print("Key:", key)

# CREATE A SYMMETRIC ENCRYPTION
cipher_suite = Fernet(key)
print("Cipher Suite", cipher_suite)

message = b"Hello World"

# ENCRYPT THE MESSAGE
cipher_text = cipher_suite.encrypt(message)
print("Encrypted: ", cipher_text)

# DECRYPT THE MESSAGE
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)
print("Decrypted: ", plain_text.decode())