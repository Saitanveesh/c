def caesar(text, key):
    ans = ""
    for c in text.upper():
        if c.isalpha():
            ans += chr((ord(c)-65+key)%26+65)
        else:
            ans += c
    return ans

text = input("Enter text: ")
key = int(input("Enter key: "))

enc = caesar(text, key)
print("Encrypted:", enc)
print("Decrypted:", caesar(enc, -key))
