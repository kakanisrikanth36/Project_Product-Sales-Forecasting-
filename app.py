from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model at startup
model = joblib.load("best_lgbm_model.pkl")

@app.route('/')
def home():
    return "✅ Sales Forecasting Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_df = pd.DataFrame([data])   # Convert JSON to DataFrame
    prediction = model.predict(input_df)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')