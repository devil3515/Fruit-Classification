from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the model
# model = tf.keras.models.load_model('fruitsInitial.h5')
import pickle

# Path to your saved model
model_path = 'model.pkl'

# Open the file in read-binary mode and load the model
with open(model_path, 'rb') as file:
    model = pickle.load(file)





# Define a function to preprocess the image
def preprocess_image(image):
    image = image.resize((150, 150))  # Resize to the size your model expects
    image = np.array(image) / 255.0   # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Define a function to make predictions
def predict_image(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    class_names = ['Apple', 'Banana', 'Grape', 'Mango', 'Strawberry']
    return class_names[predicted_class]


@app.route('/')
def fruits():
    return render_template('fruit_classification.html')

# @app.route('/fruit_classification')
# def about():
#     return render_template('fruit_classification.html')
   

# @app.route('/house_price_prediction')
# def services():
#     return render_template('house_price_prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    image = Image.open(file)
    prediction = predict_image(image)
    
    return jsonify({'prediction': prediction})





if __name__ == '__main__':
    app.run(debug=True)