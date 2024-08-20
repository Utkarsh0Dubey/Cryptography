# Diffie-Hellman Key Exchange
# Choose public parameters, prime p as 7 and generator g as 3.
p = 2**127 - 1
g = 2

# Alice, Bob choose 2 large numbers:
a, b = 10002232332324001, 20000446486102

# Alice computes her public key as:
A = pow(g, a, p)

# Bob computes his public key as:
B = pow(g, b, p)

# Alice computes the secret as (after receiving B):
s_alice = pow(B, a, p)

# Bob computes the secret as (after receiving A):
s_bob = pow(A, b, p)

print("Alice's Secret is: ", s_alice)
print("\nBob's Secret is: ", s_bob)


