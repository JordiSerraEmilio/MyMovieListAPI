from hashlib import sha256
import bcrypt

from models import user


def convert_to_sha256(text: str):
    h = sha256()
    h.update(text)
    hash_to_encrypt = h.hexdigest()
    return hash_to_encrypt


def generate_salt():
    salt = bcrypt.gensalt(16)
    return salt

