import timeit
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad

# Given message
message = b"Performance Testing of Encryption Algorithms"

# DES setup
des_key = b'8bytekey'  # DES requires an 8-byte key
des_cipher = DES.new(des_key, DES.MODE_ECB)
padded_message_des = pad(message, DES.block_size)

# AES-256 setup
aes_key = b'byteslongkeyforaesencryptiontest'  # AES-256 requires a 32-byte key
aes_cipher = AES.new(aes_key, AES.MODE_ECB)
padded_message_aes = pad(message, AES.block_size)

# Timing DES encryption
des_encryption_time = timeit.timeit(lambda: des_cipher.encrypt(padded_message_des), number=10000)

# Timing DES decryption
des_encrypted_message = des_cipher.encrypt(padded_message_des)
des_decryption_time = timeit.timeit(lambda: unpad(des_cipher.decrypt(des_encrypted_message), DES.block_size), number=10000)

# Timing AES-256 encryption
aes_encryption_time = timeit.timeit(lambda: aes_cipher.encrypt(padded_message_aes), number=10000)

# Timing AES-256 decryption
aes_encrypted_message = aes_cipher.encrypt(padded_message_aes)
aes_decryption_time = timeit.timeit(lambda: unpad(aes_cipher.decrypt(aes_encrypted_message), AES.block_size), number=10000)

# Average time per operation (dividing by the number of iterations)
print("DES Encryption Time: {:.10f} seconds".format(des_encryption_time / 10000))
print("DES Decryption Time: {:.10f} seconds".format(des_decryption_time / 10000))
print("AES-256 Encryption Time: {:.10f} seconds".format(aes_encryption_time / 10000))
print("AES-256 Decryption Time: {:.10f} seconds".format(aes_decryption_time / 10000))
