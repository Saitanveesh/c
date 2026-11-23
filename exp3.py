from PIL import Image
from pathlib import Path

if not Path("flower.png").exists():
    Image.new("RGB", (100, 100), "white").save("flower.png")

img = Image.open("flower.png").convert("RGB")
text = input("Secret: ") + "####"

bits = "".join(format(ord(c), "08b") for c in text)
data = [v for p in img.getdata() for v in p]

if len(bits) > len(data):
    raise ValueError("Image too small")

for i in range(len(bits)):
    data[i] = (data[i] & 254) | int(bits[i])

img.putdata([tuple(data[i:i+3]) for i in range(0, len(data), 3)])
img.save("stego.png")

bits = "".join(str(v & 1) for p in Image.open("stego.png").getdata() for v in p)
text = ""
for i in range(0, len(bits)-7, 8):
    text += chr(int(bits[i:i+8], 2))
    if text.endswith("####"):
        break

print("Extracted:", text[:-4])
