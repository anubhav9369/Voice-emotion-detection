# Voice Emotion Detection

## Setup
1. Clone repo
2. `pip install -r requirements.txt`
3. Download emotion dataset into `data/<emotion>` folders

## Training

# Voice Emotion Detection 🎙️

This project detects human emotions (happy, sad, angry, neutral) from recorded voice using MFCC and an LSTM model in TensorFlow.

## Features
- Real-time voice recording
- Flask API for prediction
- LSTM model trained on MFCC features

## Usage
1. Start Flask server: `python src/app.py`
2. Record and predict: `python record_predict.py`

## Author
Anubhav Verma
## License
MIT License
## Acknowledgments
- [Emotion Recognition Dataset](https://www.kaggle.com/msambare/voice-em
otion-recognition-dataset)
- [TensorFlow](https://www.tensorflow.org/)
