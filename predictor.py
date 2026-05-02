import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load
model = load_model("scam_model.h5")
tokenizer = joblib.load("tokenizer.pkl")

MAX_LEN = 20

def predict_scam(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=MAX_LEN, padding="post")

    prediction = model.predict(padded)[0][0]

    if prediction > 0.5:
        return {
            "label": "SCAM ❌",
            "confidence": f"{prediction*100:.2f}%"
        }
    else:
        return {
            "label": "SAFE ✅",
            "confidence": f"{(1-prediction)*100:.2f}%"
        }