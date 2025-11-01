# Edge TTS Gradio

Edge TTS Gradio is a lightweight, cloud-powered Python application that converts text or PDF documents into high-quality, human-like speech using [Microsoft Edge Text-to-Speech (TTS)](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech).  
Built with [Gradio](https://www.gradio.app/), it provides a browser-based interface that runs locally or in the cloud with minimal setup.

## Overview

Edge TTS Gradio combines Microsoft's neural voice technology with an intuitive web interface for effortless text-to-speech generation.  
Users can upload PDF files or paste text directly, select a preferred voice, and instantly generate `.mp3` audio output.

Use cases include:
- Narration for educational and training materials  
- Audio summaries for technical or academic documents  
- Accessibility tools for visually impaired users  
- Voice rendering for reports, notes, and research content  

## Key Features

- **PDF and Text Input** – Automatically extracts text from uploaded PDF files  
- **Microsoft Neural Voices** – Delivers realistic AI-powered speech synthesis  
- **Asynchronous Processing** – Ensures non-blocking execution and responsiveness  
- **Automatic File Management** – Generated audio is saved in the `/audios_TTS` directory  
- **Cross-Platform** – Compatible with all major operating systems supporting Python 3.8+  
- **Configurable Voices** – Easily modify or extend available voices in the configuration file  

## Requirements

Install dependencies listed in [`requirements.txt`](requirements.txt):

```bash
pip install -r requirements.txt
```

Dependencies include:
- [Gradio](https://www.gradio.app/)
- [edge-tts](https://pypi.org/project/edge-tts/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- `yaml`
- `pyprojroot`

## Project Structure

```
Edge_TTS_Gradio/
│
├── main.py                  # Main application file
├── requirements.txt         # Python dependencies
├── audios_TTS/              # Stores generated MP3 files
└── setup/
    └── config_setup.py      # Configuration for available voices
```

## Running the Application

```bash
git clone https://github.com/YourUsername/Edge_TTS_Gradio.git
cd Edge_TTS_Gradio
pip install -r requirements.txt
python main.py
```

When launched, Gradio will open a local interface such as:
```
Running on local URL: http://127.0.0.1:7860/
```

## Usage

1. Upload a PDF file *(optional)* or paste text directly.  
2. Select a preferred voice (e.g., `en-US-AndrewNeural`), default is `en-US-AndrewNeural .  
3. Enter an output filename.  
4. Click **Generate & Save** to produce the audio file.  
5. The resulting `.mp3` file appears in `/audios_TTS` and can be played or downloaded.

## Configuration

Voice settings are defined in [`setup/config_setup.py`](setup/config_setup.py). Example:

```python
config.voices = {
    "en-US-AndrewNeural": "English (US) - Andrew",
    "en-GB-LibbyNeural": "English (UK) - Libby",
    "ja-JP-NanamiNeural": "Japanese - Nanami",
    "ms-MY-YasminNeural": "Malay - Yasmin"
}
```

## Technical Notes

- **Text Extraction** uses `PyMuPDF` (`fitz`) for PDF parsing  
- **Speech Synthesis** is handled asynchronously using `edge-tts`  
- **Interface Layer** utilizes Gradio’s block-based components  
- **AsyncIO Event Loop** ensures performance and concurrency  

## Deployment Options

- **Local**: Run `python main.py`  
- **Hugging Face Spaces**: Push repository and set SDK to Gradio  
- **Render / Replit / Railway**: Use `python main.py` as the start command  

## Future Enhancements

- Display text along with audio.  
- Update voice list
