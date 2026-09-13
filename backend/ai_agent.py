import re


def analyze_data_risk(data: str):

    text = data.lower()

    score = 0

    reasons = []


    # ==========================================
    # HIGH-RISK INDICATORS
    # ==========================================

    high_risk_patterns = {

        "password": 40,

        "private key": 50,

        "secret": 40,

        "credit card": 50,

        "bank account": 50,

        "api key": 45,

        "authentication token": 45
    }


    for keyword, points in high_risk_patterns.items():

        if keyword in text:

            score += points

            reasons.append(
                f"Sensitive indicator detected: {keyword}"
            )


    # ==========================================
    # MEDIUM-RISK INDICATORS
    # ==========================================

    medium_risk_patterns = {

        "email": 20,

        "phone": 20,

        "address": 20,

        "username": 15,

        "date of birth": 25,

        "location": 20
    }


    for keyword, points in medium_risk_patterns.items():

        if keyword in text:

            score += points

            reasons.append(
                f"Personal information detected: {keyword}"
            )


    # ==========================================
    # PATTERN ANALYSIS
    # ==========================================

    # Email pattern

    if re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        text
    ):

        score += 20

        reasons.append(
            "Email address pattern detected"
        )


    # Phone number pattern

    if re.search(
        r"\b\d{10}\b",
        text
    ):

        score += 20

        reasons.append(
            "Phone number pattern detected"
        )


    # Long token / possible secret

    if re.search(
        r"\b[A-Za-z0-9]{32,}\b",
        data
    ):

        score += 30

        reasons.append(
            "Long token-like string detected"
        )


    # ==========================================
    # LIMIT SCORE
    # ==========================================

    score = min(
        score,
        100
    )


    # ==========================================
    # DETERMINE RISK LEVEL
    # ==========================================

    if score >= 60:

        risk = "HIGH"

    elif score >= 25:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    # ==========================================
    # DEFAULT REASON
    # ==========================================

    if not reasons:

        reasons.append(
            "No significant sensitive-data indicators detected"
        )


    return {

        "risk": risk,

        "score": score,

        "reason": "; ".join(
            reasons
        ),

        "indicators": reasons
    }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    test_cases = [

        "Hello CryptoGuard",

        "My email is example@gmail.com",

        "My password is secret123"
    ]


    print(
        "CryptoGuard Intelligent Risk Agent"
    )

    print(
        "=================================="
    )


    for data in test_cases:

        result = analyze_data_risk(
            data
        )

        print("\nData:")
        print(data)

        print("\nRisk:")
        print(result["risk"])

        print(
            "Score:",
            result["score"]
        )

        print(
            "Reason:",
            result["reason"]
        )