document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('spamForm');
    const emailText = document.getElementById('emailText');
    const charCount = document.getElementById('charCount');
    const resultSection = document.getElementById('result');
    const resultContent = document.getElementById('resultContent');
    const loading = document.getElementById('loading');
    const submitBtn = document.getElementById('submitBtn');

    // Character counter
    emailText.addEventListener('input', function() {
        charCount.textContent = emailText.value.length;
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        resultSection.style.display = 'none';
        resultContent.innerHTML = '';
        loading.style.display = 'block';
        submitBtn.disabled = true;

        try {
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: emailText.value })
            });
            const data = await response.json();
            loading.style.display = 'none';
            submitBtn.disabled = false;
            if (data.prediction) {
                resultSection.style.display = 'block';
                if (data.prediction === 'spam') {
                    resultContent.innerHTML = '<span class="result-icon"><i class="fas fa-exclamation-triangle"></i></span> <span class="result-spam">Spam detected! Be careful.</span>';
                } else {
                    resultContent.innerHTML = '<span class="result-icon"><i class="fas fa-check-circle"></i></span> <span class="result-not-spam">This is not spam.</span>';
                }
            } else if (data.error) {
                resultSection.style.display = 'block';
                resultContent.innerHTML = '<span class="result-icon"><i class="fas fa-times-circle"></i></span> <span class="result-spam">' + data.error + '</span>';
            } else {
                resultSection.style.display = 'block';
                resultContent.innerHTML = '<span class="result-icon"><i class="fas fa-question-circle"></i></span> <span class="result-spam">Unexpected response.</span>';
            }
        } catch (err) {
            loading.style.display = 'none';
            submitBtn.disabled = false;
            resultSection.style.display = 'block';
            resultContent.innerHTML = '<span class="result-icon"><i class="fas fa-times-circle"></i></span> <span class="result-spam">Network error. Please make sure the backend is running.</span>';
        }
    });
}); 
