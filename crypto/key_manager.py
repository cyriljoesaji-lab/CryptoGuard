import secrets
import sqlite3
from datetime import datetime, timezone

from crypto.aes_engine import generate_key


DATABASE = "cryptoguard.db"


def initialize_key_table():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encryption_keys (
            key_id TEXT PRIMARY KEY,
            created_at TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def create_key_record():

    initialize_key_table()

    key_id = secrets.token_hex(16)

    key = generate_key()

    created_at = datetime.now(
        timezone.utc
    ).isoformat()

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO encryption_keys
        (key_id, created_at, status)
        VALUES (?, ?, ?)
    """, (
        key_id,
        created_at,
        "ACTIVE"
    ))

    connection.commit()
    connection.close()

    return key_id, key


def revoke_key(key_id):

    initialize_key_table()

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE encryption_keys
        SET status = ?
        WHERE key_id = ?
    """, (
        "REVOKED",
        key_id
    ))

    connection.commit()

    updated = cursor.rowcount

    connection.close()

    return updated > 0


def rotate_key():

    initialize_key_table()

    # Revoke all currently active keys
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE encryption_keys
        SET status = ?
        WHERE status = ?
    """, (
        "ROTATED",
        "ACTIVE"
    ))

    connection.commit()

    connection.close()

    # Create a fresh key
    return create_key_record()


def get_key_status(key_id):

    initialize_key_table()

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT key_id, created_at, status
        FROM encryption_keys
        WHERE key_id = ?
    """, (
        key_id,
    ))

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return None

    return {
        "key_id": result[0],
        "created_at": result[1],
        "status": result[2]
    }


def get_all_keys():

    initialize_key_table()

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT key_id, created_at, status
        FROM encryption_keys
        ORDER BY created_at DESC
    """)

    keys = cursor.fetchall()

    connection.close()

    return [
        dict(key)
        for key in keys
    ]


if __name__ == "__main__":

    key_id, key = create_key_record()

    print("CryptoGuard Key Manager")
    print("-----------------------")

    print("New Key ID:")
    print(key_id)

    print("\nKey size:")
    print(len(key) * 8)

    print("\nKey status:")
    print(get_key_status(key_id))

    print("\nRotating key...")

    new_key_id, new_key = rotate_key()

    print("New active key:")
    print(new_key_id)

    print("\nAll keys:")

    for item in get_all_keys():
        print(item)