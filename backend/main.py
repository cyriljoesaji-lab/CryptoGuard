from pathlib import Path
import sqlite3

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from crypto.aes_engine import (
    encrypt_message,
    decrypt_message
)

from crypto.key_manager import (
    create_key_record,
    revoke_key,
    rotate_key,
    get_key_status,
    get_all_keys
)

from crypto.hmac_engine import (
    generate_hmac_key,
    create_hmac,
    verify_hmac
)

from crypto.crypto_policy import (
    get_crypto_policy
)

from crypto.ecc_engine import (
    generate_ecc_key_pair,
    sign_message,
    verify_signature
)

from backend.ai_agent import (
    analyze_data_risk
)

from backend.database import (
    create_database,
    log_security_event
)

from backend.monitor_agent import (
    analyze_security_event
)


# ==========================================
# PATH CONFIGURATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "cryptoguard.db"

FRONTEND_PATH = (
    BASE_DIR
    / "frontend"
    / "index.html"
)


# ==========================================
# FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="CryptoGuard",
    description="AI-Agent-Based Intelligent Cryptographic Security System",
    version="1.0.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ==========================================
# DATABASE INITIALIZATION
# ==========================================

create_database()


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "project": "CryptoGuard",
        "status": "online"
    }


# ==========================================
# DASHBOARD
# ==========================================

@app.get("/dashboard")
def dashboard():

    return FileResponse(
        str(FRONTEND_PATH),
        media_type="text/html"
    )


# ==========================================
# ENCRYPTION API
# ==========================================

@app.post("/encrypt")
def encrypt(data: str):

    # --------------------------------------
    # 1. AI RISK ANALYSIS
    # --------------------------------------

    risk = analyze_data_risk(data)

    risk_level = risk["risk"].lower()


    # --------------------------------------
    # 2. CRYPTOGRAPHIC POLICY
    # --------------------------------------

    policy = get_crypto_policy(
        risk_level
    )


    # --------------------------------------
    # 3. CREATE ENCRYPTION KEY
    # --------------------------------------

    key_id, encryption_key = (
        create_key_record()
    )


    # --------------------------------------
    # 4. AES-256-GCM ENCRYPTION
    # --------------------------------------

    nonce, ciphertext = encrypt_message(
        encryption_key,
        data
    )


    # --------------------------------------
    # 5. TEST DECRYPTION
    # --------------------------------------

    decrypted = decrypt_message(
        encryption_key,
        nonce,
        ciphertext
    )


    # --------------------------------------
    # 6. HMAC ACCORDING TO POLICY
    # --------------------------------------

    hmac_signature = None
    hmac_verified = None

    if policy["integrity"] == "HMAC-SHA256":

        hmac_key = generate_hmac_key()

        hmac_signature = create_hmac(
            hmac_key,
            data
        )

        hmac_verified = verify_hmac(
            hmac_key,
            data,
            hmac_signature
        )


    # --------------------------------------
    # 7. ECC DIGITAL SIGNATURE
    # --------------------------------------

    digital_signature = None
    signature_verified = None

    if policy["signature"] == "ECC-SHA256":

        private_key, public_key = (
            generate_ecc_key_pair()
        )

        digital_signature = sign_message(
            private_key,
            data
        )

        signature_verified = verify_signature(
            public_key,
            data,
            digital_signature
        )


    # --------------------------------------
    # 8. DETERMINE ALGORITHMS USED
    # --------------------------------------

    algorithms = [
        policy["encryption"]
    ]

    if policy["integrity"]:

        algorithms.append(
            policy["integrity"]
        )

    if policy["signature"]:

        algorithms.append(
            policy["signature"]
        )

    algorithm_string = " + ".join(
        algorithms
    )


    # --------------------------------------
    # 9. SECURITY EVENT LOG
    # --------------------------------------

    log_security_event(

        event_type="ENCRYPTION",

        data_sensitivity=risk["risk"],

        algorithm=algorithm_string,

        status="SUCCESS"
    )


    # --------------------------------------
    # 10. MONITORING AGENT
    # --------------------------------------

    monitoring = analyze_security_event(

        event_type="ENCRYPTION",

        status="SUCCESS",

        risk=risk["risk"]
    )


    # --------------------------------------
    # 11. RETURN RESULT
    # --------------------------------------

    return {

        "key_id": key_id,

        "original": data,

        "risk": risk["risk"],

        "risk_score": risk["score"],

        "risk_reason": risk["reason"],

        "indicators": risk["indicators"],

        "security_policy": policy,

        "encrypted": ciphertext.hex(),

        "decrypted": decrypted,

        "hmac":
            hmac_signature.hex()
            if hmac_signature
            else None,

        "hmac_verified":
            hmac_verified,

        "digital_signature":
            digital_signature.hex()
            if digital_signature
            else None,

        "signature_verified":
            signature_verified,

        "algorithm":
            algorithm_string,

        "monitoring":
            monitoring
    }


# ==========================================
# SECURITY LOGS API
# ==========================================

@app.get("/logs")
def get_logs():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()


    cursor.execute("""
        SELECT *
        FROM security_events
        ORDER BY id DESC
    """)


    logs = cursor.fetchall()

    connection.close()


    return {

        "total_events":
            len(logs),

        "events": [
            dict(log)
            for log in logs
        ]
    }


# ==========================================
# KEY MANAGEMENT API
# ==========================================

@app.get("/keys")
def list_keys():

    keys = get_all_keys()

    return {

        "total_keys":
            len(keys),

        "keys":
            keys
    }


# ==========================================
# GET KEY STATUS
# ==========================================

@app.get("/keys/{key_id}")
def key_status(
    key_id: str
):

    result = get_key_status(
        key_id
    )


    if result is None:

        return {

            "error":
                "Key not found",

            "key_id":
                key_id
        }


    return result


# ==========================================
# ROTATE KEY
# ==========================================

@app.post("/keys/rotate")
def rotate_encryption_key():

    key_id, key = rotate_key()


    return {

        "message":
            "Encryption key rotated successfully",

        "key_id":
            key_id,

        "key_size":
            len(key) * 8,

        "status":
            "ACTIVE"
    }


# ==========================================
# REVOKE KEY
# ==========================================

@app.post("/keys/{key_id}/revoke")
def revoke_encryption_key(
    key_id: str
):

    success = revoke_key(
        key_id
    )


    if not success:

        return {

            "message":
                "Key not found",

            "key_id":
                key_id,

            "status":
                "NOT_FOUND"
        }


    return {

        "message":
            "Encryption key revoked successfully",

        "key_id":
            key_id,

        "status":
            "REVOKED"
    }