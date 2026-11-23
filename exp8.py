p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))

n = p * q
phi = (p-1) * (q-1)
d = pow(e, -1, phi)

text = input("Enter text: ")

enc = []
for c in text:
    enc.append(pow(ord(c), e, n))

dec = ""
for c in enc:
    dec += chr(pow(c, d, n))

print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("Encrypted:", enc)
print("Decrypted:", dec)
