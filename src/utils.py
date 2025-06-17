import librosa
import numpy as np
import os

def extract_features(file_path, max_pad_len=174):
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast', duration=3, sr=22050, offset=0.5)
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        pad_width = max_pad_len - mfcc.shape[1]
        if pad_width > 0:
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
        else:
            mfcc = mfcc[:, :max_pad_len]
        return mfcc
    except Exception as e:
        print(f"Error extracting from {file_path}: {e}")
        return None

def load_data(data_dir='data'):
    labels = []
    features = []
    class_map = {'angry': 0, 'happy': 1, 'neutral': 2, 'sad': 3}

    for emotion in class_map:
        folder = os.path.join(data_dir, emotion)
        for file in os.listdir(folder):
            if file.endswith('.wav'):
                file_path = os.path.join(folder, file)
                mfcc = extract_features(file_path)
                if mfcc is not None:
                    features.append(mfcc)
                    labels.append(class_map[emotion])
    
    return np.array(features), np.array(labels)
