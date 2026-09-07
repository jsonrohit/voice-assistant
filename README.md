# Voice Assistant

This is a Python-based voice assistant that records audio, transcribes it into text using OpenAI's Whisper model, generates a response using Google's Generative AI, and converts the response back into speech.

## Features

- **Audio Recording**: Records 5 seconds of audio input.
- **Speech-to-Text**: Transcribes the recorded audio using OpenAI's Whisper model.
- **AI Response Generation**: Generates a response to the transcribed text using Google's Generative AI.
- **Text-to-Speech**: Converts the AI-generated response into speech and plays it back.

## Prerequisites

- Python 3.8 or higher
- MacOS (for `afplay` command to play audio)
- OpenAI Whisper model
- Google Generative AI API key
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jsonrohit/voice-assistant.git
   cd voice-assistant


## Install the required dependencies:

**Create a .env file in the project root and add your**
- GOOGLE_API_KEY="your-google-api-key"

## Usage
**Run the script:**

Speak into your microphone when prompted.

The assistant will:

- Save your audio as recording.wav.
- Transcribe the audio into text.
- Generate a response to the transcribed text.
- Convert the response into speech and play it back.

## File Structure
- main.py: The main script for the voice assistant.
- requirements.txt: Lists all the dependencies.
- .env: Stores API keys (not included in the repository).
- recording.wav: The recorded audio file.
- response.mp3: The AI-generated response in audio format.