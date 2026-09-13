\# 🛡️ CryptoGuard



\*\*AI-Assisted Cryptographic Security \& Sensitive Data Protection Platform\*\*



CryptoGuard is a security-focused application designed to provide cryptographic protection, key management, security monitoring, and configurable risk detection through a unified web-based platform.



\## 🚀 Overview



CryptoGuard combines modern cryptographic mechanisms with security monitoring and automated analysis to help protect sensitive information and provide visibility into security-related events.



The platform includes:



\* AES-based encryption

\* ECC cryptographic operations

\* HMAC-based integrity protection

\* Cryptographic key management

\* Key rotation and revocation

\* Security policy enforcement

\* Security monitoring

\* AI-assisted security analysis

\* Database-backed logging

\* REST API

\* Web-based dashboard

\* Automated security testing



\## ✨ Key Features



\### 🔐 Cryptography



\* AES encryption engine

\* Elliptic Curve Cryptography (ECC)

\* HMAC integrity protection

\* Centralized cryptographic policy

\* Secure key management



\### 🔑 Key Management



CryptoGuard provides API-based key management capabilities including:



\* Key creation/access

\* Key inspection

\* Key rotation

\* Key revocation



\### 🛡️ Security Monitoring



The monitoring component records and analyzes security-related events to provide visibility into application activity.



\### 🤖 AI-Assisted Security



CryptoGuard includes an AI agent designed to assist with security analysis and risk identification.



\### 🌐 Web API



The backend is implemented using \*\*FastAPI\*\* and exposes REST endpoints for encryption, logs, and cryptographic key management.



\## 🏗️ Project Structure



```text

CryptoGuard/

│

├── backend/

│   ├── ai\_agent.py

│   ├── database.py

│   ├── main.py

│   └── monitor\_agent.py

│

├── crypto/

│   ├── aes\_engine.py

│   ├── crypto\_policy.py

│   ├── ecc\_engine.py

│   ├── hmac\_engine.py

│   └── key\_manager.py

│

├── frontend/

│   └── index.html

│

├── tests/

│   └── test\_security.py

│

├── requirements.txt

├── README.md

└── .gitignore

```



\## 🧰 Technology Stack



| Component       | Technology                  |

| --------------- | --------------------------- |

| Backend         | Python                      |

| API Framework   | FastAPI                     |

| Server          | Uvicorn                     |

| Cryptography    | Python Cryptography Library |

| Data Validation | Pydantic                    |

| Frontend        | HTML                        |

| Testing         | Python                      |

| Database        | SQLite                      |



\## 📡 API Endpoints



\### General



| Method | Endpoint     | Purpose             |

| ------ | ------------ | ------------------- |

| GET    | `/`          | Application root    |

| GET    | `/dashboard` | Dashboard interface |



\### Encryption



| Method | Endpoint   | Purpose               |

| ------ | ---------- | --------------------- |

| POST   | `/encrypt` | Encrypt supplied data |



\### Security Logs



| Method | Endpoint | Purpose                            |

| ------ | -------- | ---------------------------------- |

| GET    | `/logs`  | Retrieve security/application logs |



\### Key Management



| Method | Endpoint                | Purpose                                   |

| ------ | ----------------------- | ----------------------------------------- |

| GET    | `/keys`                 | List available keys                       |

| GET    | `/keys/{key\_id}`        | Retrieve information about a specific key |

| POST   | `/keys/rotate`          | Rotate a cryptographic key                |

| POST   | `/keys/{key\_id}/revoke` | Revoke a specific key                     |



## 🔐 Security Methodology

CryptoGuard uses a layered cryptographic security model in which the protection applied to data is determined by its sensitivity level.

### 1. Data Sensitivity-Based Security Policy

CryptoGuard supports three security sensitivity levels:

| Sensitivity | Encryption  | Integrity   | Signature  |
| ----------- | ----------- | ----------- | ---------- |
| Low         | AES-256-GCM | —           | —          |
| Medium      | AES-256-GCM | HMAC-SHA256 | —          |
| High        | AES-256-GCM | HMAC-SHA256 | ECC-SHA256 |

All defined policies use a **256-bit AES key size**.

The policy engine is implemented in:

```text
crypto/crypto_policy.py
```

### 2. Authenticated Encryption

CryptoGuard uses **AES-256-GCM** as its encryption mechanism.

AES-GCM provides authenticated encryption, allowing encrypted data to be protected against unauthorized modification while maintaining confidentiality.

The AES implementation is located in:

```text
crypto/aes_engine.py
```

### 3. Integrity Protection

For medium- and high-sensitivity data, CryptoGuard applies:

```text
HMAC-SHA256
```

HMAC provides an integrity and authenticity mechanism that can be used to detect unauthorized modification of protected data.

### 4. Digital Signature Layer

High-sensitivity data additionally specifies:

```text
ECC-SHA256
```

as its signature mechanism.

This provides an additional cryptographic layer for high-sensitivity data.

The ECC functionality is implemented in:

```text
crypto/ecc_engine.py
```

### 5. Cryptographic Key Management

CryptoGuard includes a dedicated key-management component.

The key manager supports:

* Cryptographic key generation
* Unique key identifiers
* Key creation timestamps
* Active key tracking
* Key revocation
* Key rotation
* Key-status retrieval
* Listing of managed keys

The implementation is located in:

```text
crypto/key_manager.py
```

### 6. Key Rotation

When a key rotation operation is performed, currently active keys are marked as:

```text
ROTATED
```

A new cryptographic key is then generated and registered as:

```text
ACTIVE
```

This provides a basic key-lifecycle management mechanism.

### 7. Key Revocation

Individual keys can be revoked through the key-management system.

A revoked key receives the status:

```text
REVOKED
```

This allows CryptoGuard to maintain the lifecycle state of cryptographic keys.

### 8. Security Architecture

The overall security flow can be represented as:

```text
                    Data Input
                        │
                        ▼
                Sensitivity Level
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
            LOW       MEDIUM      HIGH
             │          │          │
             ▼          ▼          ▼
          AES-256     AES-256    AES-256
             │         + HMAC     + HMAC
             │          │         + ECC
             └──────────┼──────────┘
                        │
                        ▼
                Key Management
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
           Active    Rotated    Revoked
                        │
                        ▼
                    Database
```

### 9. Security Design Principles

CryptoGuard follows several security-oriented design principles:

* **Confidentiality** through AES-256-GCM encryption
* **Integrity protection** through HMAC-SHA256
* **Additional cryptographic assurance** for high-sensitivity data through ECC-SHA256
* **Key lifecycle management** through creation, rotation, and revocation
* **Policy-based security** through sensitivity-dependent cryptographic controls
* **Persistent key metadata** through database-backed key records
\## 🧪 Testing



Security-related functionality is tested using the project's automated test suite:



```text

tests/

└── test\_security.py

```



Tests are used to validate important security functionality and help detect regressions during development.



\## ⚠️ Project Status



CryptoGuard is currently an active development project.



Features, security policies, detection logic, and AI-assisted analysis may continue to evolve as the project develops.



\## 🔮 Future Improvements



Planned improvements may include:



\* Advanced sensitive-data detection

\* Improved contextual risk analysis

\* More cryptographic policy controls

\* Expanded monitoring capabilities

\* Enhanced AI-assisted security analysis

\* Authentication and authorization

\* Role-based access control

\* API security hardening

\* CI/CD security testing

\* Security audit logging improvements



\## 👨‍💻 Author



\*\*Cyril Joe Saji\*\*



B.Tech Computer Science \& Engineering



GitHub: \[Cyril Joe Saji](https://github.com/cyriljoesaji-lab)



\## ⚠️ Disclaimer



CryptoGuard is an educational and research-oriented cybersecurity project.



It should be properly reviewed, tested, and hardened before being used to protect sensitive information in a production environment.



\## Installation



Coming soon.



\## Usage



Coming soon.



\## Security Methodology



Coming soon.



\## Testing



Coming soon.



\## Future Improvements



\- Advanced pattern detection

\- Context-aware detection

\- Machine learning-based classification

\- CI/CD integration

## 📖 API Documentation

CryptoGuard provides a REST API through FastAPI.

When the application is running, FastAPI provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows developers to inspect available endpoints and interact with the API directly from the browser.

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides an alternative documentation interface for the API.

### Running the API

Start the backend using:

```bash
uvicorn backend.main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

### Endpoint Overview

#### `GET /`

Returns the application root response.

#### `GET /dashboard`

Provides access to the CryptoGuard dashboard.

#### `POST /encrypt`

Processes data through the application's encryption functionality.

#### `GET /logs`

Retrieves available security/application logs.

#### `GET /keys`

Retrieves the available cryptographic key information.

#### `GET /keys/{key_id}`

Retrieves information associated with a specific key.

#### `POST /keys/rotate`

Triggers cryptographic key rotation.

#### `POST /keys/{key_id}/revoke`

Revokes a specified cryptographic key.

### API Documentation Example

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface can be used to inspect request parameters, send requests, and view API responses.

