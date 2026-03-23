
import random

def encrypt(msg, key):
    
    if key == 0:
        key = random.randint(10000, 99999)
    
    out = "".join([chr((ord(c)^key)) for c in msg])

    return out, key

# x, k = encrypt("Hello World!", 0)
# print(x)

# print(encrypt(x, k))