import speech_recognition as sr

# uses audio file as source
audio_file = ("Recording.wav")

r = sr.Recognizer() # initialize the recognizer

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
# read the audio file

try:
    print("audio file contains "+ r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition did not understand the audio")
except sr.RequestError:
    print("Couldn't get the results from Google speech Recognition")


