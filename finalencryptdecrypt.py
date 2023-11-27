from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os
import time

list112 = []
list128 = []
list192 = []
list256 = []

def split_message(message, chunk_size):
    return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]

def encrypt_message(public_key, message, chunk_size):
    encrypted_chunks = []
    for chunk in split_message(message, chunk_size):
        encrypted_chunks.append(public_key.encrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ))
    return encrypted_chunks

def decrypt_message(private_key, encrypted_chunks):
    decrypted_chunks = []
    for chunk in encrypted_chunks:
        decrypted_chunks.append(private_key.decrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ))
    return b"".join(decrypted_chunks)

# 2048 112 bit

before = time.perf_counter()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048 # 2048 112 bit
)
public_key = private_key.public_key()
long_plaintext = os.urandom(10 * 1024)
long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
after = time.perf_counter()
print(f"{after - before:0.4f} seconds 2048 112 bit")

for i in range(10):
    
    #before = time.perf_counter()
    long_plaintext = os.urandom(10 * 1024)
    long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
    before = time.perf_counter()
    #after = time.perf_counter()
    long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
    after = time.perf_counter()
    list112.append(after - before)

average = sum(list112) / len(list112)
print(average, " 2048 112 bit")

# 3072 128 bit

before = time.perf_counter()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=3072 # 3072 128 bit
)

public_key = private_key.public_key()
long_plaintext = os.urandom(10 * 1024)
long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
after = time.perf_counter()
print(f"{after - before:0.4f} seconds 3072 128 bit")

for i in range(10):
    
    #before = time.perf_counter()
    long_plaintext = os.urandom(10 * 1024)
    long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
    before = time.perf_counter()
    #after = time.perf_counter()
    long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
    after = time.perf_counter()
    list128.append(after - before)

average = sum(list128) / len(list128)
print(average, " 3072 128 bit")

# 7680 192 bit

before = time.perf_counter()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=7680 # 7680 192 bit
)

public_key = private_key.public_key()
long_plaintext = os.urandom(10 * 1024)
long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
after = time.perf_counter()
print(f"{after - before:0.4f} seconds 7680 192 bit")

for i in range(10):
    
    #before = time.perf_counter()
    long_plaintext = os.urandom(10 * 1024)
    long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
    before = time.perf_counter()
    #after = time.perf_counter()
    long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
    after = time.perf_counter()
    list192.append(after - before)

average = sum(list192) / len(list192)
print(average, " 7680 192 bit")

# 15360 256 bit

before = time.perf_counter()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=15360 # 15360 256 bit
)

public_key = private_key.public_key()
long_plaintext = os.urandom(10 * 1024)
long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
after = time.perf_counter()
print(f"{after - before:0.4f} seconds 15360 256 bit")

for i in range(10):
    
    #before = time.perf_counter()
    long_plaintext = os.urandom(10 * 1024)
    long_ciphertext = encrypt_message(public_key, long_plaintext, 128)
    before = time.perf_counter()
    #after = time.perf_counter()
    long_plaintext_2 = decrypt_message(private_key, long_ciphertext)
    after = time.perf_counter()
    list256.append(after - before)

average = sum(list256) / len(list256)
print(average, " 15360 256 bit")
