document.querySelector("html").classList.add('js');

var fileInput = document.querySelector(".input-file"),
    button = document.querySelector(".input-file-trigger"),
    the_return = document.querySelector(".file-return"),
    imagePreviewContainer = document.getElementById('image-preview-container'),
    imagePreview = document.getElementById('image-preview'),
    form = document.getElementById('upload-form'),
    predictButton = document.getElementById('predict-button'),
    predictionResult = document.getElementById('prediction-result');

button.addEventListener("keydown", function(event) {
    if (event.keyCode == 13 || event.keyCode == 32) {
        fileInput.focus();
    }
});

button.addEventListener("click", function(event) {
    fileInput.focus();
    return false;
});

fileInput.addEventListener("change", function(event) {
    var file = this.files[0];
    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        };
        reader.readAsDataURL(file);
        the_return.innerHTML = file.name;
    }
});

predictButton.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission
    const formData = new FormData(form);
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction) {
            predictionResult.textContent = 'Predicted Fruit: ' + data.prediction;
            predictionResult.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
});
