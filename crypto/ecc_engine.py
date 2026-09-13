from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


def generate_ecc_key_pair():
    private_key = ec.generate_private_key(
        ec.SECP256R1()
    )

    public_key = private_key.public_key()

    return private_key, public_key


def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode("utf-8"),
        ec.ECDSA(hashes.SHA256())
    )

    return signature


def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode("utf-8"),
            ec.ECDSA(hashes.SHA256())
        )

        return True

    except Exception:
        return False


if __name__ == "__main__":

    private_key, public_key = generate_ecc_key_pair()

    message = "Welcome to CryptoGuard"

    signature = sign_message(
        private_key,
        message
    )

    print("Message:")
    print(message)

    print("\nSignature created successfully.")

    print("\nVerifying original message...")

    if verify_signature(public_key, message, signature):
        print("✅ Signature is valid.")
    else:
        print("❌ Signature is invalid.")

    tampered_message = "Welcome to CryptoHack"

    print("\nVerifying modified message...")

    if verify_signature(
        public_key,
        tampered_message,
        signature
    ):
        print("⚠️ Signature accepted.")
    else:
        print("❌ TAMPERING DETECTED!")