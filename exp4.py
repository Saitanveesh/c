def gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = gcd(b, a % b)
    return g, y, x - (a // b) * y

a = int(input("First number: "))
b = int(input("Second number: "))
print("GCD:", gcd(a, b)[0])

a = int(input("Number: "))
m = int(input("Modulus: "))
g, x, y = gcd(a, m)

if g == 1:
    print("Inverse:", x % m)
else:
    print("Inverse does not exist")
