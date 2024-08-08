document.getElementById('predict-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {};
    
    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch('/', {  // Flask endpoint'inizi kullanın
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        const prediction = result.prediction === 1 ? 'Yolcu hayatta' : 'Yolcu ölü';
        document.getElementById('prediction-result').textContent = `Tahmin edilen değer: ${prediction}`;
    })
    .catch(error => {
        console.error('Hata:', error);
    });
});