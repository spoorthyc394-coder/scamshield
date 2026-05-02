import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training dataset
data = {
    "text": [
        "You won a lottery click now",
        "Claim your free iPhone now",
        "Bank account suspended verify now",
        "Click this suspicious link",
        "Urgent OTP required",
        "Congratulations you won cash prize",
        "Free recharge offer click here",
        "Your account has been blocked verify immediately",
        "Win money instantly",
        "Exclusive reward claim now",

        "Hello how are you",
        "Meeting tomorrow at 5",
        "Let's study together",
        "Good morning friend",
        "Your package arrived",
        "Family dinner tonight",
        "Can we talk later",
        "See you in class",
        "Happy birthday",
        "Lunch at 2 PM"
    ],

    # 1 = Scam, 0 = Safe
    "label": [
        1,1,1,1,1,1,1,1,1,1,
        0,0,0,0,0,0,0,0,0,0
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Text Vectorization
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Model Training
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save trained model + vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ ScamShield model trained successfully!")
print("✅ model.pkl created")
print("✅ vectorizer.pkl created")