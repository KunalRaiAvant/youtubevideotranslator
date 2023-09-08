# YouTube Audio Processing and Transcription

## Overview

This program performs the following tasks:

1. Downloads a YouTube video
2. Extracts audio from the video
3. Splits the audio into subclips
4. Transcribes each audio subclip
5. Saves the transcription to a text file
6. Translates the transcribed text
7. Converts the translated text to speech

## Dependencies

- `pytube`
- `moviepy.editor`
- `speech_recognition`
- `googletrans`
- `gtts`

You can install these packages using pip:
\```
pip install pytube moviepy SpeechRecognition googletrans gtts
\```

## Usage

1. **Download Video**: Downloads a YouTube video using a given URL and saves it with a specified filename.
    \```python
    download_video(url, video_filename)
    \```
  
2. **Extract Audio**: Extracts audio from a video file and saves it as an audio file.
    \```python
    extract_audio(video_filename, audio_filename)
    \```
  
3. **Transcribe Audio**: Transcribes the audio using Google's speech-to-text service.
    \```python
    # Inside the main code, not a function.
    \```
  
4. **Translate and Text-to-Speech**: Translates the transcribed text and converts it to speech.
    \```python
    # Inside the main code, not a function.
    \```

### Example

To download, extract, and process a video, you can use the following lines:

\```python
url = "https://www.youtube.com/watch?v=ZLNeLC4t4jw"
video_filename = "video.mp4"
audio_filename = "audio.wav"

download_video(url, video_filename)
extract_audio(video_filename, audio_filename)
# ... (rest of the main code)
\```

## Limitations

- The program currently uses Google's speech-to-text service, which may not accurately transcribe all dialects or languages.
- Translation is done using Google Translate and may not be 100% accurate.

## License

This project is licensed under the MIT License.
