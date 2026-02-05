from datetime import datetime

def autonomous_action(result, email):
    with open("logs/detection.log", "a") as log:
        if result == "phishing":
            log.write(f"[{datetime.now()}] PHISHING DETECTED | BLOCKED | {email}\n")
            print("🚨 Autonomous Action: Email Blocked & Logged")
        else:
            log.write(f"[{datetime.now()}] SAFE EMAIL | ALLOWED | {email}\n")
            print("✅ Autonomous Action: Email Allowed")
