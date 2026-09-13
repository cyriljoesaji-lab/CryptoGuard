import sqlite3


DATABASE = "cryptoguard.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            data_sensitivity TEXT,
            algorithm TEXT,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def log_security_event(
    event_type,
    data_sensitivity,
    algorithm,
    status
):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO security_events
        (event_type, data_sensitivity, algorithm, status)
        VALUES (?, ?, ?, ?)
    """, (
        event_type,
        data_sensitivity,
        algorithm,
        status
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":

    create_database()

    print("CryptoGuard database ready.")