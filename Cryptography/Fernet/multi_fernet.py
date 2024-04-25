from cryptography.fernet import Fernet, MultiFernet

L = [Fernet(Fernet.generate_key()) for i in range(100)]
# f = MultiFernet([Fernet(key) for key in L])  # Initialize MultiFernet with Fernet instances
f = MultiFernet(L)  # Initialize MultiFernet with Fernet instances

encrypted_data = f.encrypt(b"TOR has been Hacked")
print(encrypted_data)

# Decrypt the data
decrypted_data = f.decrypt(encrypted_data)
print(decrypted_data.decode())  # Decode the bytes to string
