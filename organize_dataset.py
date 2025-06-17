import os
import shutil

# Source folder (contains Actor_01 to Actor_24)
SOURCE_DIR = '/Users/anubhavverma/Desktop/voice-emotion-detection/data/Audio_Song_Actors_01-24'
# Destination for labeled folders
DEST_DIR = 'data'

# Emotion code to label
EMOTION_MAP = {
    '01': 'neutral',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry'
}

os.makedirs(DEST_DIR, exist_ok=True)

# Traverse through actor folders
for actor in os.listdir(SOURCE_DIR):
    actor_path = os.path.join(SOURCE_DIR, actor)
    if os.path.isdir(actor_path):
        for file in os.listdir(actor_path):
            if file.endswith('.wav'):
                parts = file.split('-')
                emotion_code = parts[2]
                if emotion_code in EMOTION_MAP:
                    label = EMOTION_MAP[emotion_code]
                    target_dir = os.path.join(DEST_DIR, label)
                    os.makedirs(target_dir, exist_ok=True)
                    src_file = os.path.join(actor_path, file)
                    dst_file = os.path.join(target_dir, file)
                    shutil.copy(src_file, dst_file)

print('✅ Files organized successfully in /data/<emotion>/ folders.')
