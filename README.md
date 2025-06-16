# Audio Transcription Web App

A simple web application that uses OpenAI's Whisper model to transcribe audio files.

## Features

- Upload audio files (WAV, MP3, M4A, OGG)
- Real-time transcription using Whisper
- Modern, responsive UI
- Automatic file cleanup after transcription

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system

### Installing FFmpeg

#### macOS
```bash
brew install ffmpeg
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows
Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Click on the upload area or drag and drop an audio file
2. Wait for the transcription to complete
3. View the transcribed text below the upload area

## Supported File Formats

- WAV
- MP3
- M4A
- OGG

## Note

The first time you run the application, it will download the Whisper model, which might take a few minutes depending on your internet connection. 