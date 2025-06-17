import os
import numpy as np
from flask import Flask, request, jsonify
import tensorflow as tf
import librosa
from utils import extract_features

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('model.h5')
emotions = ['neutral', 'happy', 'sad', 'angry']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    file_path = data['path']  # Make sure it's a valid local path

    # Extract features
    mfcc = extract_features(file_path)  # shape: (40, 174)
    if mfcc is None:
        return jsonify({'error': 'Feature extraction failed'}), 400

    mfcc = np.expand_dims(mfcc, axis=0)  # shape: (1, 40, 174)
    prediction = model.predict(mfcc)[0]  # shape: (4,)
    
    return jsonify({
        'emotion': emotions[np.argmax(prediction)],
        'confidence': float(np.max(prediction))
    })
#print(f"🔎 Received file path: {data['path']}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
