import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import traceback
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Download NLTK data if not already present
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__, static_folder='../', static_url_path='')
CORS(app)

# --- Data Preprocessing Functions ---
ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

# --- Model Training at Startup ---
model = None
vectorizer = None
load_error = None
try:
    # Load data
    df = pd.read_csv('../spam.csv', encoding='latin1')
    # Drop unnecessary columns
    df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'], inplace=True)
    # Rename columns
    df.rename(columns={'v1':'target','v2':'text'}, inplace=True)
    # Encode target
    encoder = LabelEncoder()
    df['target'] = encoder.fit_transform(df['target'])
    # Remove duplicates
    df = df.drop_duplicates(keep='first')
    # Transform text
    df['transformed_text'] = df['text'].apply(transform_text)
    # Vectorization
    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(df['transformed_text']).toarray()
    y = df['target'].values
    # Train model
    model = MultinomialNB()
    model.fit(X, y)
    print("--- Model and vectorizer trained successfully at startup! ---")
except Exception as e:
    load_error = traceback.format_exc()
    print(f"!!! ERROR TRAINING MODEL: {load_error} !!!")

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
        if model is None or vectorizer is not None:
            return jsonify({'error': 'Model or vectorizer not loaded', 'details': load_error}), 500
        # Preprocess input text
        transformed = transform_text(text)
        vect_text = vectorizer.transform([transformed]).toarray()
        pred = model.predict(vect_text)[0]
        result = 'spam' if pred == 1 else 'not spam'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': 'Unknown error', 'details': traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
