import pytube
import moviepy.editor

def download_video(url, filename):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(filename)

def extract_audio(video_file, audio_file):
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file, codec='pcm_s16le')

url = "https://www.youtube.com/watch?v=ZLNeLC4t4jw"
video_filename = "video.mp4"
audio_filename = "audio.wav"

#download_video(url, video_filename)
#extract_audio(video_filename, audio_filename)
video = moviepy.editor.VideoFileClip(video_filename)
audio = video.audio
audio1 = audio.subclip(0, 60)
audio1.write_audiofile("audio1.wav", codec='pcm_s16le')
import speech_recognition as sr

r = sr.Recognizer()
audio1 = sr.AudioFile("audio1.wav")

with audio1 as source:
    audio_text = r.record(source)
    
try:
    text = r.recognize_google(audio_text, language='ta-IN')
    print("Transcribed Text:", text)
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
import os

total_length = audio.duration
subclip_length = 60
num_subclips = int(total_length / subclip_length)
num_subclips = int(total_length / subclip_length)

for i in range(num_subclips):
    start_time = i * subclip_length
    end_time = (i + 1) * subclip_length
    audio_subclip = audio.subclip(start_time, end_time)
    audio_subclip.write_audiofile(f"audio_subclip{i}.wav", codec='pcm_s16le')
with open("translation.txt", "w") as file:
    start_time = i * subclip_length
    end_time = (i + 1) * subclip_length
    audio_subclip = audio.subclip(start_time, end_time)
    
    try:
        text = r.recognize_google(audio_subclip, language='ta-IN')
        print("Transcribed Text:", text)
        file.write(text + "\n")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    progress = (i + 1) / num_subclips * 100
    print("Progress: {:.2f}%".format(progress))




os.remove("audio1.wav")
from googletrans import Translator
from gtts import gTTS

translator = Translator()
translated_text = translator.translate(text, dest='en').text

tts = gTTS(text=translated_text, lang='en')
tts.save("english_speech.mp3")


