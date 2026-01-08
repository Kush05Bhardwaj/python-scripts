# AudioBook Converter

A simple Python script that converts PDF books into audiobooks by reading the text content aloud using text-to-speech technology.

## Features

- **PDF to Speech**: Converts PDF documents into spoken audio
- **Page-by-page Reading**: Reads through all pages of the PDF sequentially
- **File Selection Dialog**: Easy-to-use file picker for selecting PDF files
- **Text Extraction**: Automatically extracts text from PDF pages

## Prerequisites

Before running this script, make sure you have Python installed on your system.

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:

```bash
pip install pyttsx3 PyPDF2
```

**Note**: There's a typo in the current script - it imports `pyttxs3` but should be `pyttsx3`. Make sure to install the correct package.

## Dependencies

- **pyttsx3**: Text-to-speech conversion library
- **PyPDF2**: PDF file reader and parser
- **tkinter**: GUI library for file dialog (usually comes with Python)

## Usage

1. Run the script:
```bash
python script.py
```

2. A file dialog will open - select the PDF file you want to convert to audio

3. The script will begin reading the PDF content page by page

4. The audio will play through your default audio output device

## How It Works

1. Opens a file selection dialog using tkinter
2. Reads the selected PDF file using PyPDF2
3. Extracts text from each page sequentially
4. Converts the extracted text to speech using pyttsx3
5. Plays the audio in real-time

