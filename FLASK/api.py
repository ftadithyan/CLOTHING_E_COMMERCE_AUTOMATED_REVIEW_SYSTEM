from flask import Flask, request, jsonify
import joblib
import os
import re

app = Flask(__name__)

# ---------------- Load model & vectorizer ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "LogisticRegression.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)

# ---------------- Sentiment to numeric mapping ----------------
SENTIMENT_MAP = {"negative": 0, "neutral": 1, "positive": 2}

# ---------------- Text cleaning function ----------------
def clean_text(text):
    text = text.lower()                          # lowercase
    text = re.sub(r'http\S+|www\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)     # remove punctuation & numbers
    text = text.strip()
    return text

# ---------------- Home route ----------------
@app.route("/", methods=["GET"])
def home():
    return "<h2>Flask API running! Use POST /predict with JSON.</h2>"

# ---------------- Predict route ----------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        name = data.get("name", "Unknown")
        review = data.get("review", "")

        if not review.strip():
            return jsonify({"error": "Review text is empty"}), 400

        # Clean review text
        review_clean = clean_text(review)

        # Transform and predict
        review_vec = tfidf.transform([review_clean])
        prediction = model.predict(review_vec)[0]   # 'negative', 'neutral', 'positive'
        numeric_rating = SENTIMENT_MAP.get(prediction, -1)

        # Return JSON
        return jsonify({
            "name": name,
            "review": review,
            "predicted_sentiment": prediction,
            "predicted_rating": numeric_rating
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- Run Flask ----------------
if __name__ == "__main__":
    app.run(debug=True)
