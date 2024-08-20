from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Hash import SHA256

# Step 1: Key Generation
key = ElGamal.generate(2048, random.get_random_bytes)
p = key.p
g = key.g
h = key.y
x = key.x

# Public key: (p, g, h)
# Private key: x

# Step 2: Encrypt the message using the public key
message = b"Confidential Data"
m = bytes_to_long(message)

# Generate a random k
k = random.StrongRandom().randint(1, p - 2)

# Compute ciphertext: (c1, c2)
c1 = pow(g, k, p)
c2 = (m * pow(h, k, p)) % p

# Step 3: Decrypt the ciphertext using the private key
# Compute m = (c2 * (c1^x)^-1) % p
s = pow(c1, x, p)
m_decrypted = (c2 * pow(s, p - 2, p)) % p  # Using modular inverse of s

# Convert decrypted message back to bytes
decrypted_message = long_to_bytes(m_decrypted)

# Print results
print("Original message:", message)
print("Ciphertext:", (c1, c2))
print("Decrypted message:", decrypted_message)
