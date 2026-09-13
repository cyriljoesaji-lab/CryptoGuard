import hmac
import hashlib
import secrets


def generate_hmac_key():
    """Generate a secure random HMAC key."""
    return secrets.token_bytes(32)


def create_hmac(key, message):
    """Create an HMAC-SHA256 signature."""

    return hmac.new(
        key,
        message.encode("utf-8"),
        hashlib.sha256
    ).digest()


def verify_hmac(key, message, signature):
    """Verify an HMAC-SHA256 signature."""

    expected_signature = create_hmac(
        key,
        message
    )

    return hmac.compare_digest(
        expected_signature,
        signature
    )


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    key = generate_hmac_key()

    message = "Welcome to CryptoGuard"

    signature = create_hmac(
        key,
        message
    )

    print("Original message:")
    print(message)

    print("\nHMAC created successfully.")

    # Verify original message
    print("\nChecking original message...")

    if verify_hmac(key, message, signature):
        print("✅ Message is authentic.")
    else:
        print("❌ Message verification failed.")

    # -----------------------------------------
    # SIMULATE TAMPERING
    # -----------------------------------------

    tampered_message = "Welcome to CryptoHack"

    print("\nChecking modified message...")
    print("Modified message:")
    print(tampered_message)

    if verify_hmac(key, tampered_message, signature):
        print("⚠️ Message accepted.")
    else:
        print("❌ TAMPERING DETECTED!")
        print("The message was modified.")