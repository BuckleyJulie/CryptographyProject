from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os
import time

list80 = []
list112 = []
list128 = []
list192 = []
list256 = []

message = os.urandom(10 * 1024)

# 1024 80 bit
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024 # 1024 80 bit
)

public_key = private_key.public_key()

# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    before = time.perf_counter()
    #after = time.perf_counter()
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    after = time.perf_counter()
    list80.append(after - before)

average = sum(list80) / len(list80)
print(average, " 1024 80 bit")

# 2048 112 bit
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048 # 2048 112 bit
)

public_key = private_key.public_key()

# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    before = time.perf_counter()
    #after = time.perf_counter()
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    after = time.perf_counter()
    list112.append(after - before)

average = sum(list112) / len(list112)
print(average, " 2048 112 bit")

# 3072 128 bit
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=3072 # 3072 128 bit
)

public_key = private_key.public_key()

# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    before = time.perf_counter()
    #after = time.perf_counter()
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    after = time.perf_counter()
    list128.append(after - before)

average = sum(list128) / len(list128)
print(average, " 3072 128 bit")

# 7680 192 bit
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=7680 # 7680 192 bit
)

public_key = private_key.public_key()

# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    before = time.perf_counter()
    #after = time.perf_counter()
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    after = time.perf_counter()
    list192.append(after - before)

average = sum(list192) / len(list192)
print(average, " 7680 192 bit")

# 15360 256 bit
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=15360 # 15360 256 bit
)

public_key = private_key.public_key()

# We can sign the message using "hash-then-sign".
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# We can verify the signature.  If the signature is invalid it will
# raise an Exception.
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

for x in range(10):
    #before = time.perf_counter()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    before = time.perf_counter()
    #after = time.perf_counter()
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    after = time.perf_counter()
    list256.append(after - before)

average = sum(list256) / len(list256)
print(average, " 15360 256 bit")
