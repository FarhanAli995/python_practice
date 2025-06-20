from pydub import AudioSegment
import os

# Load the .opus audio file
audio_path = "/mnt/data/WhatsApp Audio 2025-06-10 at 04.59.55_fb944155.opus"
audio = AudioSegment.from_file(audio_path, format="opus")

# Convert the audio to wav format for transcription compatibility
converted_path = "/mnt/data/converted_audio.wav"
audio.export(converted_path, format="wav")

converted_path
