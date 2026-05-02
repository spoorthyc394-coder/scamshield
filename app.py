from flask import Flask, render_template, request, jsonify
from model import predict

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        data = request.get_json()

        # Get user text
        text = data.get("text", "").strip()

        # Empty check
        if not text:
            return jsonify({
                "error": "Please enter some text to analyze."
            }), 400

        # Run scam detection
        result = predict(text)

        return jsonify({
            "prediction": result["label"],
            "confidence": result["confidence"],
            "reasons": result["reasons"]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# Run server 
if __name__ == "__main__":
    app.run(debug=True, port=5000)