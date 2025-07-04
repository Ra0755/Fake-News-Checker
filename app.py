from flask import Flask, request, jsonify
import joblib

# Load model and vectorizer
model = joblib.load("C:/Users/hp/OneDrive/Desktop/fake-news-checker/notebook/model.pkl")
vectorizer = joblib.load("C:/Users/hp/OneDrive/Desktop/fake-news-checker/notebook/vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Fake News Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"error": "No title provided"}), 400

    # Transform the title using the vectorizer
    title_vec = vectorizer.transform([title])
    prediction = model.predict(title_vec)[0]

    result = "This news is real" if prediction == 1 else "This news is fake"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
