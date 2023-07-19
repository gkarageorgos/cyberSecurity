from base64 import b64decode
from cryptography.hazmat.primitives import serialization
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# Open the file and read its contents
with open('pubkey.pem', 'rb') as key_file:
    pem_public_key = key_file.read()

key_file.close()

# Load the PEM-encoded public key
public_key = serialization.load_pem_public_key(pem_public_key)

# Extract the public numbers from the RSA public key
public_numbers = public_key.public_numbers()

e = public_numbers.e
n = public_numbers.n

# http://factordb.com/
p = 398075086424064937397125500550386491199064362342526708406385189575946388957261768583317
q = 472772146107435302536223071973048224632914695302097116459852171130520711256363590397527
phi = (p - 1) * (q - 1)

# private key
d = pow(e, -1, phi)

# Construct private key
priv_key = RSA.construct((n, e, d, p, q))

# Decrypt cipher
cipher_b64 = "e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA"
cipher_text = b64decode(cipher_b64)

cipher = PKCS1_v1_5.new(priv_key)
decrypt_text = cipher.decrypt(cipher_text, None).decode("UTF-8")
print(decrypt_text)
