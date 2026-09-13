def get_crypto_policy(data_sensitivity):
    if data_sensitivity == "high":
        return {
            "encryption": "AES-256-GCM",
            "integrity": "HMAC-SHA256",
            "signature": "ECC-SHA256",
            "key_size": 256
        }

    elif data_sensitivity == "medium":
        return {
            "encryption": "AES-256-GCM",
            "integrity": "HMAC-SHA256",
            "signature": None,
            "key_size": 256
        }

    else:
        return {
            "encryption": "AES-256-GCM",
            "integrity": None,
            "signature": None,
            "key_size": 256
        }


if __name__ == "__main__":

    sensitivity = "high"

    policy = get_crypto_policy(sensitivity)

    print("Data sensitivity:")
    print(sensitivity)

    print("\nCryptoGuard security policy:")

    for key, value in policy.items():
        print(f"{key}: {value}")