from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Nạp mô hình đã huấn luyện
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "🏠 Dự đoán giá nhà API đang chạy!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({
            "predicted_price": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
