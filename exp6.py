from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b'1234567890abcdef'
text = input("Enter text: ").encode()

cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(text, 16))

cipher = AES.new(key, AES.MODE_ECB)
dec = unpad(cipher.decrypt(enc), 16)

print("Encrypted:", base64.b64encode(enc).decode())
print("Decrypted:", dec.decode())
