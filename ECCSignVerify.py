from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import os
import time

list96 = []
list112 = []
list128 = []
list192 = []
list256 = []

message = os.urandom(10 * 1024) #10KB

# 96 Bit
private_key = ec.generate_private_key(
    ec.SECP192R1()
)

public_key = private_key.public_key()
# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    ec.ECDSA(hashes.SHA256())
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    #after = time.perf_counter()
    before = time.perf_counter()
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after = time.perf_counter()
    list96.append(after - before)

average = sum(list96) / len(list96)
print(average, " 96 bit")

# 112 Bit
private_key = ec.generate_private_key(
    ec.SECP224R1()
)

public_key = private_key.public_key()
# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    ec.ECDSA(hashes.SHA256())
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    #after = time.perf_counter()
    before = time.perf_counter()
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after = time.perf_counter()
    list112.append(after - before)

average = sum(list112) / len(list112)
print(average, " 112 bit")

# 128 Bit
private_key = ec.generate_private_key(
    ec.SECP224R1()
)

public_key = private_key.public_key()
# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    ec.ECDSA(hashes.SHA256())
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    #after = time.perf_counter()
    before = time.perf_counter()
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after = time.perf_counter()
    list128.append(after - before)

average = sum(list128) / len(list128)
print(average, " 128 bit")

# 192 Bit
private_key = ec.generate_private_key(
    ec.SECP384R1()
)

public_key = private_key.public_key()
# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    ec.ECDSA(hashes.SHA256())
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    #after = time.perf_counter()
    before = time.perf_counter()
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after = time.perf_counter()
    list192.append(after - before)

average = sum(list192) / len(list192)
print(average, " 192 bit")

# 256 Bit
private_key = ec.generate_private_key(
    ec.SECP521R1()
)

public_key = private_key.public_key()
# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    ec.ECDSA(hashes.SHA256())
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    #after = time.perf_counter()
    before = time.perf_counter()
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after = time.perf_counter()
    list256.append(after - before)

average = sum(list256) / len(list256)
print(average, " 256 bit")
