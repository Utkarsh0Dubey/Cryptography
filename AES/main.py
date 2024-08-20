from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Given key: (16 bit)
key = b'0123456789ABCDEF'

# Given message:
message = b"Sensitive Information"

# Creation of AES cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Padding the message:
padded_message = pad(message, AES.block_size)

# Encryption:
encrypted_message = cipher.encrypt(padded_message)

print("Encrypted message is:")
print(encrypted_message)

# Decryption:
decrypted_message = cipher.decrypt(encrypted_message)
unpadded_message = unpad(decrypted_message, AES.block_size)
print("On Decryption, we get:")
print(unpadded_message)

