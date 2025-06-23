import pickle
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import os

app = Flask(__name__, static_folder='../', static_url_path='')
CORS(app)

print("--- Attempting to load models from backend/ directory ---")
try:
    # Load model and vectorizer
    with open('vectorizer.pkl', 'rb') as f_vect:
        vectorizer = pickle.load(f_vect)
    with open('model.pkl', 'rb') as f_model:
        model = pickle.load(f_model)
    print("--- Models loaded successfully! ---")
except Exception as e:
    print(f"!!! ERROR LOADING MODELS: {e} !!!")
    vectorizer = None
    model = None

@app.route('/')
def index():
    return send_from_directory('../', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../', path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    if model is None or vectorizer is None:
        return jsonify({'error': 'Model or vectorizer not loaded. Check server logs.'}), 500

    # Vectorize
    vect_text = vectorizer.transform([text]).toarray()
    # Predict
    pred = model.predict(vect_text)[0]
    result = 'spam' if pred == 1 else 'not spam'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
