import pickle
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import os

# Load model and vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__, static_folder='../', static_url_path='')
CORS(app)

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
    # Vectorize
    vect_text = vectorizer.transform([text]).toarray()
    # Predict
    pred = model.predict(vect_text)[0]
    result = 'spam' if pred == 1 else 'not spam'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
