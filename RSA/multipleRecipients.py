from base64 import b64decode
from libnum import nroot, solve_crt
from cryptography.hazmat.primitives import serialization
from Crypto.Util.number import long_to_bytes, bytes_to_long


def pubkey(pem):
    # Open the file and read its contents
    with open(pem, 'rb') as key_file:
        pem_public_key = key_file.read()

    # Load the PEM-encoded public key
    public_key = serialization.load_pem_public_key(pem_public_key)

    # Extract the public numbers from the RSA public key
    public_numbers = public_key.public_numbers()
    return public_numbers


def enc_mes(message):
    return bytes_to_long(b64decode(open(message, "rb").read()))


n1 = pubkey('clef0_pub.pem').n
n2 = pubkey('clef1_pub.pem').n
n3 = pubkey('clef2_pub.pem').n
e = 3

c1 = enc_mes('m0')
c2 = enc_mes('m1')
c3 = enc_mes('m2')

mod = [n1, n2, n3]
c = [c1, c2, c3]

msg = solve_crt(c, mod)
m = nroot(msg, e)
print(long_to_bytes(m))
