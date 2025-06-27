# Email Spam Classifier

A modern, official, and attractive web app to classify emails or SMS as spam or not spam using AI.

## Features
- Clean, responsive frontend
- Flask backend with live model training (no pickle files needed)
- Uses your provided `spam.csv` for model training
- Easy to use and extend

---

## Setup Instructions

### 1. Clone or Download the Project
Make sure you have all files including `spam.csv` in the root directory.

### 2. Backend Setup
1. Open terminal in the project root.
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Start the backend server:
   ```bash
   python backend/app.py
   ```
   The backend will train the model from `spam.csv` at startup.

### 3. Frontend Usage
1. Open `index.html` in your browser (double-click or right-click > Open with browser).
2. Paste any email or SMS content and click **Analyze**.
3. See the result instantly!

---

## Project Structure
```
Email Spam Classifier/
  backend/
    app.py
    requirements.txt
  spam.csv
  index.html
  styles.css
  script.js
  README.md
```

---

## Notes
- Make sure the backend is running before using the frontend.
- The backend runs on `http://localhost:5000` by default.
- You can customize the frontend design in `styles.css`.
- The backend will always use the latest `spam.csv` for training.

---

## Credits
- Built with ❤️ using Flask, scikit-learn, and modern web tech. 