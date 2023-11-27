from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
import os
import time

list80 = []
list112 = []
list128 = []
list140 = []

message = os.urandom(10 * 1024) #10KB

# 1024 80 bit

private_key = dsa.generate_private_key(
    key_size=1024 # 1024 80 bit
)

public_key = private_key.public_key()

for x in range(10):
    before = time.perf_counter()
    private_key = dsa.generate_private_key(
        key_size=1024 # 1024 80 bit
    )

    public_key = private_key.public_key()
    after = time.perf_counter()
    list80.append(after - before)

average = sum(list80) / len(list80)
print(average, " 1024 80 bit")

# 2048 112 bit

private_key = dsa.generate_private_key(
    key_size=2048 # 2048 112 bit
)

public_key = private_key.public_key()

for x in range(10):
    before = time.perf_counter()
    private_key = dsa.generate_private_key(
        key_size=2048 # 2048 112 bit
    )

    public_key = private_key.public_key()
    after = time.perf_counter()
    list112.append(after - before)

average = sum(list112) / len(list112)
print(average, " 2048 112 bit")

# 3072 128 bit

private_key = dsa.generate_private_key(
    key_size=3072 # 3072 128 bit
)

public_key = private_key.public_key()
for x in range(10):
    before = time.perf_counter()
    private_key = dsa.generate_private_key(
        key_size=3072 # 3072 128 bit
    )

    public_key = private_key.public_key()
    after = time.perf_counter()
    list128.append(after - before)

average = sum(list128) / len(list128)
print(average, " 3072 128 bit")

# 4096 140 bit

private_key = dsa.generate_private_key(
    key_size=4096 # 4096 140 bit
)

public_key = private_key.public_key()
for x in range(10):
    before = time.perf_counter()
    private_key = dsa.generate_private_key(
        key_size=4096 # 4096 140 bit
    )

    public_key = private_key.public_key()
    after = time.perf_counter()
    list140.append(after - before)

average = sum(list140) / len(list140)
print(average, " 4096 140 bit")
