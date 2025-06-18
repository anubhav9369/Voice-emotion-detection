# Use slim image with Python 3.10
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install OS dependencies (for librosa, soundfile, etc.)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    libasound2-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy all files
COPY . .

# Upgrade pip and install Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 10000

# Start your app
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
