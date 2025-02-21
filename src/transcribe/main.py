import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def cli():
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file using OpenAI's Whisper."
    )
    parser.add_argument("audio_file", help="Path to the audio file to transcribe.")
    args = parser.parse_args()

    audio_file_path = args.audio_file
    if not os.path.exists(audio_file_path):
        print(f"Error: file '{audio_file_path}' not found.")
        sys.exit(1)

    # Perform transcription
    print(f"Transcribing '{audio_file_path}'...")
    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file
    )
    transcript = transcription.text

    # Create an output text file with the same name (but .txt extension)
    base_name = os.path.splitext(audio_file_path)[0]
    output_file = f"{base_name}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"Transcription saved to '{output_file}'")
