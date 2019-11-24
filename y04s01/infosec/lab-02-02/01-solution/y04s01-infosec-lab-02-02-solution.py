import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


def run_compute_hash(text):
    """Computes the SHA-256 sum of the given string.
    """
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(text.encode())
    res = digest.finalize()
    print(
        "Plain text:  {}\n"
        "SHA-256 sum: {}\n"
        .format(
            text,
            res.hex(),
        )
    )


def run_aead_chacha(plaintext, associated_data=""):
    """Encrypts and decrypts given plaintext using ChaCha20Poly1305 AEAD.
    """
    data = plaintext.encode()
    aad = associated_data.encode()
    key = ChaCha20Poly1305.generate_key()
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    ciphertext = chacha.encrypt(nonce, data, aad)
    decrypted_text = chacha.decrypt(nonce, ciphertext, aad)

    print(
        "Plaintext:      {}\n"
        "Ciphertext:     {}\n"
        "Decrypted text: {}"
        .format(
            plaintext,
            ciphertext,
            decrypted_text,
        )
    )


if __name__ == "__main__":
    text = input("Text: ")
    run_compute_hash(text)
    run_aead_chacha(text)
