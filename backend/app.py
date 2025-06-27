import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import traceback
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
from sklearn.linear_model import LogisticRegression

# Download NLTK data if not already present
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)
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
    # Robust path for spam.csv
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spam.csv')
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"spam.csv not found at {csv_path}. Please ensure the file exists in the project root.")
    df = pd.read_csv(csv_path, encoding='latin1')
    df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'], inplace=True)
    df.rename(columns={'v1':'target','v2':'text'}, inplace=True)
    encoder = LabelEncoder()
    df['target'] = encoder.fit_transform(df['target'])
    df = df.drop_duplicates(keep='first')
    df['transformed_text'] = df['text'].apply(transform_text)
    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(df['transformed_text']).toarray()
    y = df['target'].values
    # Train/test split for accuracy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    model_accuracy = accuracy_score(y_test, y_pred)
    print(f"--- Model and vectorizer trained successfully at startup! Accuracy: {model_accuracy:.4f} ---")
except Exception as e:
    load_error = traceback.format_exc()
    print(f"!!! ERROR TRAINING MODEL: {load_error} !!!")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        if model is None or vectorizer is None:
            return jsonify({'error': 'Model or vectorizer not loaded', 'details': load_error}), 500
        transformed = transform_text(text)
        vect_text = vectorizer.transform([transformed]).toarray()
        pred = model.predict(vect_text)[0]
        result = 'spam' if pred == 1 else 'not spam'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': 'Unknown error', 'details': traceback.format_exc()}), 500

@app.route('/metrics')
def metrics():
    if 'model_accuracy' in globals():
        return jsonify({'accuracy': model_accuracy})
    else:
        return jsonify({'error': 'Accuracy not available'}), 500

@app.route('/')
def home():
    return {'status': 'ok', 'message': 'Email Spam Classifier Backend Running!'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
