# Encryption Function:
def encrypt(message, n, e):
    result = []
    for char in message:
        m = ord(char) - ord('a')
        c = pow(m, e, n)
        result.append(c)
    return result

# Decryption Function:
def decrypt(encryption, n, d):
    result = ""
    for c in encryption:
        m = pow(c, d, n)
        result += chr(m + ord('a'))
    return result

# Main program
def main():

    # Choosing the 2 primes:
    p, q = 97, 31
    # Product of numbers , n = p * q
    # Public key is: (n, e)
    n = p * q
    e = 65537

    # Private key is: (n, d)
    phi_n = (p - 1) * (q - 1)
    d = pow(e, - 1, phi_n)

    # Encrypt:
    encryption = encrypt("unyielding resolve through darkness", n, e)
    print(encryption)
    # Decrypt:
    decryption = decrypt(encryption, n, d)
    print("On decryption, we get:")
    print(decryption)


# Run the main program
if __name__ == "__main__":
    main()
