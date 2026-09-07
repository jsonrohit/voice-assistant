from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from gtts import gTTS
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Load your .env file credentials
load_dotenv()

sample_rate = 44100
duration = 5

print("🎤 Speak now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()
write("recording.wav", sample_rate, audio)
print("✅ Recording saved!")

print("##########  Transcribing audio file... (this may take a moment)##########")
# 1. Load the Whisper model (options: tiny, base, small, medium, large)
# 'base' strikes a good balance between speed and accuracy
model = whisper.load_model("small")
# 2. Transcribe the audio file
result = model.transcribe("recording.wav",fp16=False)

if result["text"]:
    print("✅ Transcription successful!")
else:
    print("❌ Transcription failed. Please try again.")

# 3. Print the text result
print("\nTranscription Result:")
print(result["text"])

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.7)
response = llm.invoke(result["text"])
print(response.content)

text_result = response.content[0]['text']
# 2. Check if text was found
if not text_result:
    reply = "Transcription completed, but the audio file appears to be silent."
    print(f"⚠️ {reply}")
else:
    reply = f"Here is your transcription: {text_result}"
    print(f"\n📝 {reply}")

# 3. Convert text reply to speech and play it on Mac
tts = gTTS(text=reply, lang='en')
tts.save("response.mp3")

# 'afplay' is the built-in Mac audio player command
os.system("afplay response.mp3") 