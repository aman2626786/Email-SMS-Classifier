import pickle
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import os
import traceback

app = Flask(__name__, static_folder='../', static_url_path='')
CORS(app)

print("--- Attempting to load models from backend/ directory ---")
model = None
vectorizer = None
load_error = None
try:
    with open('vectorizer.pkl', 'rb') as f_vect:
        vectorizer = pickle.load(f_vect)
    with open('model.pkl', 'rb') as f_model:
        model = pickle.load(f_model)
    print("--- Models loaded successfully! ---")
except Exception as e:
    load_error = traceback.format_exc()
    print(f"!!! ERROR LOADING MODELS: {load_error} !!!")

@app.route('/health')
def health():
    if model is not None and vectorizer is not None:
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error', 'details': load_error}), 500

@app.route('/')
def index():
    return send_from_directory('../', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../', path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        if model is None or vectorizer is None:
            return jsonify({'error': 'Model or vectorizer not loaded', 'details': load_error}), 500

        try:
            vect_text = vectorizer.transform([text]).toarray()
        except Exception as ve:
            return jsonify({'error': 'Vectorization failed', 'details': traceback.format_exc()}), 500

        try:
            pred = model.predict(vect_text)[0]
        except Exception as me:
            return jsonify({'error': 'Prediction failed', 'details': traceback.format_exc()}), 500

        result = 'spam' if pred == 1 else 'not spam'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': 'Unknown error', 'details': traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
