import General
import os
import K_PKE

q = 3329

# Generate a random 32-byte value
random_bytes = os.urandom(32)

ek, dk = (K_PKE.KeyGen(random_bytes))

ciphertext = K_PKE.Encrypt(ek,"Hello, world!", random_bytes)

