import os
import sounddevice as sd
from scipy.io.wavfile import write
import requests

DURATION = 3
SAMPLERATE = 22050
FILENAME = "recorded.wav"
FULL_PATH = os.path.abspath(FILENAME)
API_URL = "http://127.0.0.1:5001/predict"

print("🎙️ Speak now... Recording for 3 seconds")
recording = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
sd.wait()
write(FILENAME, SAMPLERATE, recording)
print("✅ Recording saved as", FULL_PATH)

print("📤 Sending to model for prediction...")
response = requests.post(API_URL, json={"path": FULL_PATH})

if response.ok:
    result = response.json()
    print(f"\n🔍 Detected Emotion: {result['emotion'].upper()} (Confidence: {round(result['confidence']*100, 2)}%)")
else:
    print("❌ Error:", response.text)
