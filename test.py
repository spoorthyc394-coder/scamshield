import requests

# Flask API URL
url = "http://127.0.0.1:5000/predict"

# Test messages
test_cases = [
    "Congratulations! You won 50,000 cash prize. Click now http://fake-link.com",
    "Your bank account is suspended. Verify OTP immediately.",
    "Call me at +91 9876543210",
    "Hello, how are you doing today?",
    "Let's meet tomorrow for lunch."
]

print("🚀 ScamShield PRO API Test\n")

for i, message in enumerate(test_cases, start=1):
    try:
        response = requests.post(url, json={"text": message})

        print(f"Test Case {i}:")
        print("Message:", message)

        if response.status_code == 200:
            result = response.json()

            print("Prediction:", result.get("prediction"))
            print("Confidence:", result.get("confidence"))

            reasons = result.get("reasons", [])
            print("Reasons:")
            for reason in reasons:
                print("-", reason)

        else:
            print("Error:", response.json())

    except Exception as e:
        print("Server connection failed:", str(e))

    print("-" * 50)