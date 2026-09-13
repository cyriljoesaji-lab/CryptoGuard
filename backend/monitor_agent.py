def analyze_security_event(
    event_type,
    status,
    risk
):

    alerts = []

    if status != "SUCCESS":
        alerts.append("Security operation failed.")

    if risk == "HIGH":
        alerts.append("High-risk data detected.")

    if event_type == "TAMPERING":
        alerts.append("Possible data tampering detected.")

    if alerts:
        return {
            "alert": True,
            "messages": alerts
        }

    return {
        "alert": False,
        "messages": []
    }


if __name__ == "__main__":

    result = analyze_security_event(
        "ENCRYPTION",
        "SUCCESS",
        "HIGH"
    )

    print("CryptoGuard Monitoring Agent")
    print("----------------------------")
    print(result)