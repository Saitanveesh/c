text = input("Enter text: ").replace(" ", "").upper()
key = int(input("Enter key: "))

while len(text) % key:
    text += "X"

enc = ""
for i in range(key):
    enc += text[i::key]

dec = ""
rows = len(text) // key
for i in range(rows):
    dec += enc[i::rows]

print("Encrypted:", enc)
print("Decrypted:", dec.rstrip("X"))
