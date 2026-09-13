import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key():
    """Generate a random 256-bit AES key."""
    return AESGCM.generate_key(bit_length=256)


def encrypt_message(key, message):
    """Encrypt a message using AES-256-GCM."""

    aes = AESGCM(key)

    # AES-GCM commonly uses a 12-byte nonce
    nonce = os.urandom(12)

    message_bytes = message.encode("utf-8")

    ciphertext = aes.encrypt(
        nonce,
        message_bytes,
        None
    )

    return nonce, ciphertext


def decrypt_message(key, nonce, ciphertext):
    """Decrypt an AES-256-GCM encrypted message."""

    aes = AESGCM(key)

    decrypted_bytes = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return decrypted_bytes.decode("utf-8")


# Test the functions
if __name__ == "__main__":

    key = generate_key()

    message = "Welcome to CryptoGuard"

    nonce, ciphertext = encrypt_message(
        key,
        message
    )

    decrypted_message = decrypt_message(
        key,
        nonce,
        ciphertext
    )

    print("Original:")
    print(message)

    print("\nEncrypted:")
    print(ciphertext)

    print("\nDecrypted:")
    print(decrypted_message)