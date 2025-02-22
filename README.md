# Trascribe

This is a demonstration on how to transform OpenAPI speech-to-text Quickstart code into a local installable CLI to transcribe audio files.

## Install

**Using [uv](https://docs.astral.sh/uv/) (recommended)**
```
uv tool install .
```

**Using pip**
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install .
```

## Usage

Export your OpenAI secret key and against an audio file.

```bash
# If you used pip, remind activating the venv
export OPENAI_API_KEY="sk-proj-openaikey123"
transcribe path/to/audio.mp3
```

Which will create a transcription in `path/to/audio.txt`
