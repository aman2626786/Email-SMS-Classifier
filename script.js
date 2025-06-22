// DOM elements
const spamForm = document.getElementById('spamForm');
const emailText = document.getElementById('emailText');
const charCount = document.getElementById('charCount');
const submitBtn = document.getElementById('submitBtn');
const result = document.getElementById('result');
const resultContent = document.getElementById('resultContent');
const loading = document.getElementById('loading');

// Character counter
emailText.addEventListener('input', function() {
    const count = this.value.length;
    charCount.textContent = count;
    
    // Change color based on length
    if (count > 1000) {
        charCount.style.color = '#d63031';
    } else if (count > 500) {
        charCount.style.color = '#fdcb6e';
    } else {
        charCount.style.color = '#666';
    }
});

// Form submission
spamForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const text = emailText.value.trim();
    
    if (!text) {
        showError('Please enter some email content to analyze.');
        return;
    }
    
    if (text.length < 10) {
        showError('Please enter at least 10 characters for accurate analysis.');
        return;
    }
    
    // Show loading state
    showLoading();
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        showResult(data.prediction);
        
    } catch (error) {
        console.error('Error:', error);
        showError('An error occurred while analyzing the email. Please try again.');
    }
});

// Show loading state
function showLoading() {
    result.style.display = 'none';
    loading.style.display = 'block';
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
}

// Hide loading state
function hideLoading() {
    loading.style.display = 'none';
    submitBtn.disabled = false;
    submitBtn.innerHTML = '<i class="fas fa-search"></i> Analyze Email';
}

// Show result
function showResult(prediction) {
    hideLoading();
    
    const isSpam = prediction.toLowerCase() === 'spam';
    const icon = isSpam ? 'fas fa-exclamation-triangle' : 'fas fa-check-circle';
    const message = isSpam ? 'This email appears to be SPAM!' : 'This email appears to be legitimate.';
    const className = isSpam ? 'result-spam' : 'result-not-spam';
    
    resultContent.innerHTML = `
        <div class="result-icon">
            <i class="${icon}"></i>
        </div>
        <div>
            <strong>${message}</strong>
            <br>
            <small>Confidence: ${isSpam ? 'High' : 'High'} - AI Analysis Complete</small>
        </div>
    `;
    
    resultContent.className = `result-content ${className}`;
    result.style.display = 'block';
    
    // Scroll to result
    result.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Show error
function showError(message) {
    hideLoading();
    
    resultContent.innerHTML = `
        <div class="result-icon">
            <i class="fas fa-exclamation-circle"></i>
        </div>
        <div>
            <strong style="color: #d63031;">Error</strong>
            <br>
            <small>${message}</small>
        </div>
    `;
    
    resultContent.className = 'result-content result-spam';
    result.style.display = 'block';
}

// Add some sample emails for testing
const sampleEmails = [
    {
        title: "Legitimate Email",
        content: "Hi John, I hope this email finds you well. I wanted to follow up on our meeting from last week regarding the project timeline. Please let me know if you have any questions or if we need to schedule another meeting. Best regards, Sarah"
    },
    {
        title: "Spam Email", 
        content: "CONGRATULATIONS! You've won $1,000,000! Click here to claim your prize NOW! Limited time offer! Don't miss this amazing opportunity! ACT FAST before it expires!"
    }
];

// Add sample buttons (optional - for testing)
function addSampleButtons() {
    const sampleContainer = document.createElement('div');
    sampleContainer.className = 'sample-buttons';
    sampleContainer.style.cssText = `
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        justify-content: center;
    `;
    
    sampleEmails.forEach((sample, index) => {
        const button = document.createElement('button');
        button.textContent = `Sample ${index + 1}: ${sample.title}`;
        button.style.cssText = `
            padding: 8px 16px;
            border: 2px solid #667eea;
            background: white;
            color: #667eea;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        `;
        
        button.addEventListener('mouseenter', () => {
            button.style.background = '#667eea';
            button.style.color = 'white';
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.background = 'white';
            button.style.color = '#667eea';
        });
        
        button.addEventListener('click', () => {
            emailText.value = sample.content;
            emailText.dispatchEvent(new Event('input'));
        });
        
        sampleContainer.appendChild(button);
    });
    
    // Insert before the form
    spamForm.parentNode.insertBefore(sampleContainer, spamForm);
}

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    // Add sample buttons for testing (uncomment if you want them)
    // addSampleButtons();
    
    // Focus on textarea
    emailText.focus();
    
    // Add some nice animations
    const cards = document.querySelectorAll('.info-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.style.animation = 'fadeInUp 0.6s ease-out forwards';
        card.style.opacity = '0';
    });
});

// Add CSS for sample buttons
const style = document.createElement('style');
style.textContent = `
    .sample-buttons {
        margin-bottom: 20px;
    }
    
    .sample-buttons button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
`;
document.head.appendChild(style); 