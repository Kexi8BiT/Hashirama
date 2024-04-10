from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
import json

def derive_key(password):
    salt = bytes("salt", encoding="utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_file(filename, data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open(filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(filename, key):
    try:
        with open(filename, 'rb') as f:
            encrypted_data = f.read()
    except:
        return "404"

    cipher = Fernet(key)
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except:
        return "418"

    # with open(filename[:-10], 'wb') as f:  # Remove ".encrypted" extension
    #     f.write(decrypted_data)
    print("Готово")
    return decrypted_data
