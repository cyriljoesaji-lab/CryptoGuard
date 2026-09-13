from crypto.aes_engine import (
    generate_key,
    encrypt_message,
    decrypt_message
)

from crypto.hmac_engine import (
    generate_hmac_key,
    create_hmac,
    verify_hmac
)

from crypto.ecc_engine import (
    generate_ecc_key_pair,
    sign_message,
    verify_signature
)


print("======================================")
print("      CryptoGuard Security Tests")
print("======================================")


# ==========================================
# TEST 1 — AES ENCRYPTION
# ==========================================

print("\n[TEST 1] AES-256-GCM Encryption")

key = generate_key()

message = "CryptoGuard Security Test"

nonce, ciphertext = encrypt_message(
    key,
    message
)

decrypted = decrypt_message(
    key,
    nonce,
    ciphertext
)

if decrypted == message:

    print("PASS - Encryption and decryption successful")

else:

    print("FAIL - Decrypted data does not match")


# ==========================================
# TEST 2 — AES TAMPERING DETECTION
# ==========================================

print("\n[TEST 2] AES Tampering Detection")

tampered_ciphertext = bytearray(ciphertext)

tampered_ciphertext[0] ^= 1

try:

    decrypt_message(
        key,
        nonce,
        bytes(tampered_ciphertext)
    )

    print("FAIL - Tampered ciphertext was accepted")

except Exception:

    print("PASS - Tampering detected")


# ==========================================
# TEST 3 — HMAC VERIFICATION
# ==========================================

print("\n[TEST 3] HMAC Integrity Verification")

hmac_key = generate_hmac_key()

signature = create_hmac(
    hmac_key,
    message
)

if verify_hmac(
    hmac_key,
    message,
    signature
):

    print("PASS - Original message verified")

else:

    print("FAIL - Original message rejected")


# ==========================================
# TEST 4 — HMAC TAMPERING
# ==========================================

print("\n[TEST 4] HMAC Tampering Detection")

modified_message = (
    "CryptoGuard Modified Test"
)

if verify_hmac(
    hmac_key,
    modified_message,
    signature
):

    print("FAIL - Modified message accepted")

else:

    print("PASS - Modified message rejected")


# ==========================================
# TEST 5 — DIGITAL SIGNATURE
# ==========================================

print("\n[TEST 5] ECC Digital Signature")

private_key, public_key = (
    generate_ecc_key_pair()
)

digital_signature = sign_message(
    private_key,
    message
)

if verify_signature(
    public_key,
    message,
    digital_signature
):

    print("PASS - Digital signature verified")

else:

    print("FAIL - Digital signature rejected")


# ==========================================
# TEST 6 — SIGNATURE TAMPERING
# ==========================================

print("\n[TEST 6] Digital Signature Tampering")

modified_message = (
    "CryptoGuard Modified Test"
)

if verify_signature(
    public_key,
    modified_message,
    digital_signature
):

    print("FAIL - Modified message accepted")

else:

    print("PASS - Signature tampering detected")


# ==========================================
# SUMMARY
# ==========================================

print("\n======================================")
print("        Security Testing Complete")
print("======================================")