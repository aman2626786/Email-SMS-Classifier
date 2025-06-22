# Email/SMS Spam Classifier 🛡️

A sophisticated machine learning-powered web application designed to detect and classify spam emails and SMS messages with high accuracy. Built with modern web technologies and advanced NLP techniques.

## 📋 Project Overview

This project addresses the critical need for automated spam detection in digital communication. With the increasing volume of unwanted emails and SMS messages, this classifier provides a reliable solution using machine learning algorithms to distinguish between legitimate messages and spam.

### 🎯 Key Objectives
- **Automated Detection**: Instantly classify emails/SMS as spam or legitimate
- **High Accuracy**: Achieve 97%+ accuracy in spam detection
- **User-Friendly Interface**: Modern, responsive web design
- **Real-time Processing**: Instant results with optimized performance
- **Privacy-First**: Secure processing without data storage

## 🚀 Features

### Core Functionality
- **AI-Powered Classification**: Uses Multinomial Naive Bayes algorithm with TF-IDF vectorization
- **Real-time Analysis**: Instant prediction results
- **High Accuracy**: 97.39% accuracy with 99.06% precision
- **Text Preprocessing**: Advanced NLP techniques for better classification

### User Experience
- **Modern UI/UX**: Beautiful, responsive design with smooth animations
- **Mobile Responsive**: Optimized for all devices and screen sizes
- **Intuitive Interface**: Simple text input with clear results display
- **Visual Feedback**: Color-coded results and confidence indicators

### Technical Features
- **RESTful API**: Clean backend architecture with Flask
- **CORS Support**: Cross-origin resource sharing enabled
- **Error Handling**: Robust error management and user feedback
- **Scalable Design**: Modular architecture for easy maintenance

## 🏗️ Architecture

### Frontend Stack
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with Grid and Flexbox
- **Vanilla JavaScript**: Lightweight, fast client-side logic
- **Font Awesome**: Professional icons
- **Google Fonts**: Typography optimization

### Backend Stack
- **Flask**: Lightweight Python web framework
- **scikit-learn**: Machine learning library
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation
- **Pickle**: Model serialization

### Machine Learning Pipeline
- **TF-IDF Vectorization**: Text feature extraction
- **Multinomial Naive Bayes**: Classification algorithm
- **Data Preprocessing**: Text cleaning and normalization
- **Model Persistence**: Trained model storage and loading

## 📊 Performance Metrics

The model achieves excellent performance across multiple metrics:

- **Accuracy**: 97.39%
- **Precision**: 99.06%
- **Recall**: 80.15%
- **F1-Score**: 88.61%

## 🗂️ Project Structure

```
Email Spam Classifier/
├── backend/
│   ├── app.py              # Flask server with API endpoints
│   ├── requirements.txt    # Python dependencies
│   ├── model.pkl          # Trained ML model
│   └── vectorizer.pkl     # TF-IDF vectorizer
├── index.html             # Main application interface
├── styles.css             # Modern CSS styling
├── script.js              # Frontend JavaScript logic
├── spam.csv               # Training dataset
└── README.md              # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Modern web browser

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Email-Spam-Classifier
   ```

2. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser
   - Navigate to `http://localhost:5000`
   - Start classifying emails/SMS!

## 📱 Usage Guide

### For End Users
1. **Open the website** in your preferred browser
2. **Paste email/SMS content** into the text area
3. **Click "Analyze Message"** to get instant results
4. **Review the prediction** with confidence indicators

### For Developers
The application provides a RESTful API for integration:

```javascript
// Example API call
fetch('/predict', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        text: "Your email content here"
    })
})
.then(response => response.json())
.then(data => console.log(data.prediction));
```

## 🔧 API Documentation

### Endpoints

#### `GET /`
- **Purpose**: Serves the main application interface
- **Response**: HTML page with the spam classifier interface

#### `POST /predict`
- **Purpose**: Analyzes text content for spam classification
- **Request Body**: `{"text": "content to analyze"}`
- **Response**: `{"prediction": "spam" | "not spam"}`

### Error Handling
- **400 Bad Request**: Missing or invalid text input
- **500 Internal Server Error**: Server-side processing errors

## 🎨 Customization

### Styling Modifications
- Edit `styles.css` to customize colors, fonts, and layout
- Modify CSS variables for easy theme changes
- Adjust responsive breakpoints for different screen sizes

### Functionality Extensions
- Add new features in `script.js`
- Implement additional ML models in the backend
- Extend API endpoints for enhanced functionality

### Model Improvements
- Replace `model.pkl` and `vectorizer.pkl` with custom models
- Implement ensemble methods for better accuracy
- Add support for multiple languages

## 🔍 Technical Details

### Machine Learning Implementation
- **Algorithm**: Multinomial Naive Bayes
- **Feature Extraction**: TF-IDF with 3000 vocabulary size
- **Data Preprocessing**: Text cleaning, normalization, and vectorization
- **Model Training**: Cross-validation with proper train-test split

### Data Pipeline
- **Input**: Raw text content
- **Preprocessing**: Text cleaning and normalization
- **Feature Engineering**: TF-IDF vectorization
- **Classification**: ML model prediction
- **Output**: Spam/Not Spam classification

### Performance Optimization
- **Model Caching**: Pre-trained models for fast inference
- **API Optimization**: Efficient request handling
- **Frontend Optimization**: Minimal JavaScript for fast loading
- **Responsive Design**: Optimized for all devices

## 🚨 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port already in use**
   - Change port in `app.py`: `app.run(port=5001)`

3. **Model files missing**
   - Ensure `model.pkl` and `vectorizer.pkl` are in the backend directory

4. **CORS errors**
   - Check browser console for detailed error messages
   - Verify CORS configuration in Flask app

### Performance Issues
- **Slow predictions**: Check model file size and optimization
- **Memory issues**: Monitor system resources during operation
- **Network errors**: Verify API endpoint accessibility

## 🔮 Future Enhancements

### Planned Features
- **Multi-language Support**: Classification in multiple languages
- **Advanced Analytics**: Detailed spam pattern analysis
- **User Feedback**: Learning from user corrections
- **API Rate Limiting**: Enhanced security and performance
- **Model Versioning**: Support for multiple model versions

### Technical Improvements
- **Deep Learning Models**: Integration with neural networks
- **Real-time Learning**: Continuous model improvement
- **Cloud Deployment**: Scalable cloud infrastructure
- **Mobile App**: Native mobile application

## 🤝 Contributing

We welcome contributions to improve this project:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Contribution Areas
- **UI/UX Improvements**: Better user interface design
- **Model Enhancements**: Improved ML algorithms
- **Documentation**: Better code and user documentation
- **Testing**: Comprehensive test coverage
- **Performance**: Optimization and speed improvements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Created by Aman Sharma**

## 🙏 Acknowledgments

- **Dataset**: Original spam dataset contributors
- **Open Source**: Community libraries and frameworks
- **Testing**: Beta testers and feedback providers

---

**Built with ❤️ for a spam-free digital world**

*This project demonstrates the power of machine learning in solving real-world problems and provides a foundation for building more sophisticated spam detection systems.* 