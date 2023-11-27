from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os
import time

list80 = []
list112 = []
list128 = []
list192 = []
list256 = []


def Average(lst):
    return sum(lst) / len(lst)

# 1024 = 80-bit security
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024 # 1024 = 80-bit security
)

public_key = private_key.public_key()


for x in range(10):
    before = time.perf_counter()   
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024 # 1024 = 80-bit security
        )
    
    public_key = private_key.public_key()
    after = time.perf_counter()
    list80.append(after - before)

average80 = Average(list80)
print(average80, "80-bit")

# 2048 = 112-bit security
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048 # 2048 = 112-bit security
)

public_key = private_key.public_key()


for x in range(10):
    before = time.perf_counter()   
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048 # 2048 = 112-bit security
        )
    
    public_key = private_key.public_key()
    after = time.perf_counter()
    list112.append(after - before)

average112 = Average(list112)
print(average112, "112-bit")

# 3072 = 128-bit security
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=3072 # 3072 = 128-bit security
)

public_key = private_key.public_key()


for x in range(10):
    before = time.perf_counter()   
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=3072 # 3072 = 128-bit security
        )
    
    public_key = private_key.public_key()
    after = time.perf_counter()
    list128.append(after - before)

average128 = Average(list128)
print(average128, "128-bit")

# 7680 = 192-bit security
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=7680 # 7680 = 192-bit security
)

public_key = private_key.public_key()


for x in range(10):
    before = time.perf_counter()   
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=7680 # 7680 = 192-bit security
        )
    
    public_key = private_key.public_key()
    after = time.perf_counter()
    list192.append(after - before)

average192 = Average(list192)
print(average192, "192-bit")

# 15360 = 256-bit security
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=15360 # 15360 = 256-bit security
)

public_key = private_key.public_key()


for x in range(10):
    before = time.perf_counter()   
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=15360 # 15360 = 256-bit security
        )
    
    public_key = private_key.public_key()
    after = time.perf_counter()
    list256.append(after - before)

average256 = Average(list256)
print(average256, "256-bit")
