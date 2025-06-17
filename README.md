# 🎙️ Voice Emotion Detection

This is a real-time voice emotion detection project built using Python, TensorFlow/Keras, Flask, and audio signal processing with MFCC features. It can record your voice, process it, and classify your emotion into one of: **neutral**, **happy**, **sad**, or **angry**.

## 🔧 Features

- 🎤 Real-time voice recording
- 🤖 Emotion prediction using trained LSTM model
- 🌐 REST API built with Flask
- 📊 Uses MFCC features extracted from audio
- ✅ Supports `.wav` files for prediction

## 🧠 Emotions Detected

- Neutral 😐  
- Happy 😄  
- Sad 😢  
- Angry 😠  

## 🛠️ Tech Stack

- Python
- TensorFlow/Keras
- Librosa
- Flask
- SoundDevice (for audio recording)

## 📦 Folder Structure
voice-emotion-detection/
│
├── data/ # Training data
├── models/ # Trained models (ignored in Git)
├── src/ # Main source code
│ ├── app.py # Flask API
│ ├── model.py # LSTM model builder
│ ├── train.py # Training script
│ ├── utils.py # Feature extraction and data loader
├── record_predict.py # Records audio and sends to API
├── .gitignore
├── README.md


## 🚀 How to Run

### 1. Train the Model (Optional if model already trained)
``bash``
cd src
python train.py

### 2. Start the Flask Server
bash
Copy
Edit
python app.py

### 3. Record and Predict Emotion
bash
Copy
Edit
python record_predict.py

## 🧪 Sample Output
css
Copy
Edit
🎙️ Speak now... Recording for 3 seconds
✅ Recording saved as recorded.wav
📤 Sending to model for prediction...
🎯 Detected Emotion: happy (Confidence: 0.92)
