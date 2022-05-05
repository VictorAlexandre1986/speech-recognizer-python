#instalação:
# pip install SpeechRecognition
# pipwin install PyAudio

import speech_recognition as sr

rec =  sr.Recognizer()

#Vai retornar uma lista com os microfones
print(sr.Microphone.list_microphone_names())

#Colocar o indice do microfone
with sr.Microphone(0) as mic:
    #Elimina os ruidos do ambiente
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar:")
    #Ouve o audio
    audio = rec.listen(mic)

with open('resultado.wav',wb) as file:
    file.write(audio.get_wav_data())
