import re
import joblib

# Load trained ML files
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Suspicious scam keywords
suspicious_keywords = [
    "lottery", "prize", "winner", "click now", "urgent",
    "verify", "bank", "otp", "free", "cash", "claim",
    "reward", "offer", "money", "blocked", "suspended"
]


# Detect suspicious links
def contains_suspicious_link(text):
    url_pattern = r"(https?://[^\s]+|www\.[^\s]+)"
    return re.search(url_pattern, text.lower()) is not None


# Detect phone numbers
def contains_phone_number(text):
    phone_pattern = r"(\+?\d[\d\s\-\(\)]{7,}\d)"
    return re.search(phone_pattern, text) is not None


# Detect emails
def contains_email(text):
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.search(email_pattern, text) is not None


# Keyword score
def keyword_score(text):
    text_lower = text.lower()
    return sum(1 for word in suspicious_keywords if word in text_lower)


# Main prediction function
def predict(text):
    reasons = []
    score = 0

    # ML prediction
    X = vectorizer.transform([text])
    ml_prediction = model.predict(X)[0]

    if ml_prediction == 1:
        score += 2
        reasons.append("Scam-like language detected")

    # Link detection
    if contains_suspicious_link(text):
        score += 2
        reasons.append("Suspicious link detected")

    # Phone detection
    if contains_phone_number(text):
        score += 1
        reasons.append("Phone number detected")

    # Email detection
    if contains_email(text):
        score += 1
        reasons.append("Email address detected")

    # Keyword detection
    kw_score = keyword_score(text)
    if kw_score > 0:
        score += kw_score
        reasons.append("Suspicious keywords detected")

    # Final label
    if score >= 4:
        label = "SCAM ❌"
    elif score >= 2:
        label = "SUSPICIOUS ⚠️"
    else:
        label = "SAFE ✅"

    confidence = min(score * 20, 99)

    return {
        "label": label,
        "confidence": f"{confidence}%",
        "reasons": reasons if reasons else ["No major scam indicators found"]
    }