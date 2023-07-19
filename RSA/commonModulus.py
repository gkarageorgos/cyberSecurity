from base64 import b64decode
from Crypto.Util.number import long_to_bytes, bytes_to_long
from cryptography.hazmat.primitives import serialization


def pubkey(pem):
    # Open the file and read its contents
    with open(pem, 'rb') as key_file:
        pem_public_key = key_file.read()

    key_file.close()

    # Load the PEM-encoded public key
    public_key = serialization.load_pem_public_key(pem_public_key)

    # Extract the public numbers from the RSA public key
    public_numbers = public_key.public_numbers()
    return public_numbers.e, public_numbers.n


def enc_mes(message):
    return bytes_to_long(b64decode(open(message, "rb").read()))


e1, n1 = pubkey('key1_pub.pem')
e2, n2 = pubkey('key2_pub.pem')
# print(n1 == n2)
n = n1

c1 = enc_mes('message1')
c2 = enc_mes('message2')


def gcd(a, b):
    newx, x, newy, y = 0, 1, 1, 0
    while b:
        a, (q, b) = b, divmod(a, b)
        newx, x = x - q * newx, newx
        newy, y = y - q * newy, newy
    return a, x, y


gcd, x, y = gcd(e1, e2)

m = (pow(c1, x, n) * pow(c2, y, n)) % n
print(long_to_bytes(m))
