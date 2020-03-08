import random
import math


def is_prime(num):
    if num == 2:
        return True
    elif num < 2:
        return False
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)), 2):
            if num%i == 0:
                return False
    return True


def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        q = a // m
        t = m

        # m is the remainder
        # same as the Euclid's gcd() algorithm
        m = a % m
        a = t
        t = y

        # update x and y accordingly
        y = x - q * y
        x = t

        # make sure x>0 so x is positive
    if (x < 0):
        x = x + m0
    return x


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_keys():
    p = random.randint(1e3, 1e5)
    while not is_prime(p):
        p = random.randint(1e3, 1e5)
    q = random.randint(1e3, 1e5)
    while not is_prime(q):
        q = random.randint(1e3, 1e5)
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = modular_inverse(e, phi)
    return p, q, e, d


def encrypt(plain, pub, n):
    cipher = []
    for char in plain:
        a = ord(char)
        cipher.append(pow(a, pub, n))
    return cipher


def decrypt(cipher, priv, n):
    plain = ''
    for num in cipher:
        a = pow(num, priv, n)
        plain = plain + str(chr(a))
    return plain


key, key2, pub_key, priv_key = generate_keys()
key_n = key*key2
print("Public Key: ", pub_key)
print("Private Key: ", priv_key)
cipher_text = encrypt(input("Enter Plain Text"), pub_key, key_n)
print("Cipher: ", cipher_text)
plain_text = decrypt(cipher_text, priv_key, key_n)
print("Plain Text: ", plain_text)
