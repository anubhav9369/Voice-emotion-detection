from utils import load_data
from model import build_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint
import numpy as np

# Load MFCC features
X, y = load_data('/Users/anubhavverma/Desktop/voice-emotion-detection/data')
# Do NOT add channel dimension for LSTM
# X.shape -> (num_samples, 40, 174)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train model
model = build_model((X.shape[1], X.shape[2]))  # input_shape = (40, 174)
model.summary()

checkpoint = ModelCheckpoint('model.h5', monitor='val_accuracy', save_best_only=True, mode='max')
model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test), callbacks=[checkpoint])

# Save model (optional since checkpoint is saved)
model.save("final_model.h5")
