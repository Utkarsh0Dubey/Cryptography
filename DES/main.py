from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Given key:
key = b'A1B2C3D4'
# Given message:
message = b'Confidential Data'

# Creation of DES cipher object
# As a mode of operation, we use ECB (Electronic Codebook)
cipher = DES.new(key, DES.MODE_ECB)

# Padding the message to fit the block size.
# Needed when message is not multiple of 8 bytes.
padded_message = pad(message, DES.block_size)
# Above, DES,block_size = 64 = constant.

ciphertext = cipher.encrypt(padded_message)

print("The ciphertext is:")
print(ciphertext)

decrypted_message = cipher.decrypt(ciphertext)
unpadded_message = unpad(decrypted_message, DES.block_size)
print("On decryption, we get:")
print(unpadded_message)

