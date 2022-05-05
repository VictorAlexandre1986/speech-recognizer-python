#instalação:
# pip install SpeechRecognition
# pipwin install PyAudio

import speech_recognition as sr
from os import path
audio_file=path.join(path.dirname(path.realpath("examples_english.wav")))

rec =  sr.Recognizer()

with sr.AudioFile(audio_file)as source:
    audio = rec.record(source)
    texto = rec.recognize_google(audio, language="pt-BR")




