import os
import asyncio
import fitz  # PyMuPDF
import gradio as gr
from edge_tts import Communicate
from setup.config_setup import Config
import re

config = Config()  # config.voices = list of voices
print(config.voices)

# Folder for saving audio files
OUTPUT_FOLDER = "audios_TTS"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Async TTS function
async def text_to_speech(text, output_file, voice="en-US-AndrewNeural"):
    communicate = Communicate(text, voice=voice)
    await communicate.save(output_file)
    return output_file

# Main pipeline
def generate_tts(pdf_file, text_input, filename, voice):
    # Decide source of text
    if pdf_file is not None:
        doc = fitz.open(pdf_file.name)
        text = ""
        for page in doc:
            text += page.get_text("text")
    else:
        text = text_input
    
    if not text.strip():
        return None
    
    # Clean text
    text = " ".join(text.split())
    text = re.sub(r"[#*]+", " ", text).strip()
    
    # Build output file path
    filename = filename.strip() if filename else "output"
    output_file = os.path.join(OUTPUT_FOLDER, f"{filename}.mp3")
    
    # Run async TTS
    asyncio.run(text_to_speech(text, output_file, voice))
    
    return output_file

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("PDF/Text to Speech Converter")
    
    with gr.Row():
        pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
        text_input = gr.Textbox(label="Or Paste Text", lines=10, placeholder="Enter text here...")
    
    with gr.Row():
        filename_input = gr.Textbox(label="Output File Name (without extension)", placeholder="e.g. lecture_notes")
        voice_selector = gr.Dropdown(choices= list(config.voices.items()), value="en-US-AndrewNeural", label="Select Voice")
    
    generate_btn = gr.Button("Generate & Save")
    clear_btn = gr.Button("Clear")
    
    audio_output = gr.Audio(label="Preview Audio", type="filepath")
    
    # Bind buttons
    generate_btn.click(
        fn=generate_tts,
        inputs=[pdf_input, text_input, filename_input, voice_selector],
        outputs=[audio_output]
    )
    clear_btn.click(
        fn=lambda: (None, "", "", "en-US-AndrewNeural", None),
        inputs=[],
        outputs=[pdf_input, text_input, filename_input, voice_selector, audio_output]
    )

# Launch
if __name__ == "__main__":
    demo.launch()
