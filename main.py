#our main file.

import speech_recognition as sr
# criar um reconhecedor
r =sr.Recognizer()
#abrir o microfone para captura
with sr.Microphone() as source:
    audio = r.listen(source) 
    #define microfone como fonte de audio
    while True:
        print(r.recognize_google(audio))