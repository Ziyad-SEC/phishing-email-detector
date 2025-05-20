import re

def is_phishing(email_content):
    suspicious_phrases = [
        "verify your account",
        "urgent action required",
        "click here to update",
        "your account will be suspended",
        "you won a prize"
    ]
    for phrase in suspicious_phrases:
        if phrase.lower() in email_content.lower():
            return True
    return False

email = """
Hello,

You have won a prize! Click here to claim: http://phishy.link
"""

if is_phishing(email):
    print("⚠️ Phishing detected! Quarantining email...")
    with open("logs/quarantine.log", "a") as log:
        log.write(email + "\n---\n")
else:
    print("✅ Email is clean.")
