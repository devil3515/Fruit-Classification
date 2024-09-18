# 🍎🍌 **Fruit Classification Using CNN** 🍇🍓

This project uses a custom **Convolutional Neural Network (CNN)** to classify images of fruits into 5 different categories: **Apple, Banana, Grape, Mango,** and **Strawberry**. The model is trained on a labeled dataset of fruit images and achieves **85% accuracy** in distinguishing between different fruit types.

## 🚀 **Project Overview**
The goal of this project is to build a deep learning model capable of accurately identifying fruit types from images. We preprocess the data, build the CNN model, train it, and then deploy the model in a web interface where users can upload images for real-time predictions.

## 📝 **Features**
- **Data Preprocessing**: Resizing, normalization, and augmentation of images to prepare them for model training.
- **CNN Model**: A custom-built CNN architecture with multiple convolutional layers, pooling layers, and fully connected layers.
- **Model Evaluation**: The model is evaluated using accuracy, confusion matrix, and loss metrics.
- **Web Interface**: A simple web application using **Flask** where users can upload images and receive real-time predictions.
- **User-Friendly Prediction Button**: Allows users to classify fruit images and see the results displayed in large text.

## 🖥️ **Tech Stack**
- **Python**: Core programming language for model development and data processing.
- **TensorFlow/Keras**: For building and training the CNN model.
- **Pandas & NumPy**: For data handling and preprocessing.
- **Matplotlib & Seaborn**: For visualizing model performance and data insights.
- **Flask**: Web framework used for creating the web interface.
- **Jupyter Notebooks**: For experimentation and documentation of the project.

## 🧰 **Setup Instructions**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fruit-classification-cnn.git
   cd fruit-classification-cnn
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download the dataset**: You can find the dataset [here](#) or use any publicly available fruit dataset.
4. **Train the model**:
   ```bash
   python train_model.py
   ```
5. **Run the web app**:
   ```bash
   python app.py
   ```
6. **Access the web interface**:
   Open your browser and go to `http://localhost:5000`, upload an image, and get predictions.

## 🏅 **Results**
- Achieved **85% accuracy** on the test dataset.
- Confusion matrix and evaluation metrics highlight the model's effectiveness in classifying fruits.

## 📊 **Model Architecture**
The CNN model consists of:
- **Convolutional Layers**: For feature extraction from images.
- **Pooling Layers**: To reduce dimensionality and retain essential features.
- **Fully Connected Layers**: For final classification based on extracted features.

## 💡 **Future Improvements**
- **Expand Dataset**: Include more fruit categories and a larger dataset for improved accuracy.
- **Enhance Web App**: Add a drag-and-drop feature for easier image uploads and more interactive UI.

## 🙌 **Contributions**
Feel free to submit pull requests or open issues if you find any bugs or want to contribute to improving the model or web app.

### Happy Classifying! 🍎🍇
