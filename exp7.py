from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

key = b'1234567890abcdef'
text = input("Enter text: ").encode()

for mode in ["ECB", "CBC"]:
    iv = get_random_bytes(16)

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv)

    enc = cipher.encrypt(pad(text, 16))

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv)

    dec = unpad(cipher.decrypt(enc), 16)

    print(mode, "Encrypted:", base64.b64encode(enc).decode())
    print(mode, "Decrypted:", dec.decode())
