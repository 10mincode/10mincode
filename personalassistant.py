import wikipedia
import webbrowser
import pyttsx3
import speech_recognition as sr
import os
from datetime import datetime

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',140)
wish=""
timeget=datetime.now().hour

if timeget<12:
    wish="good Morning"
elif timeget==12:
    wish="Good Noon"
elif 12<timeget<16:
    wish="Good AfterNoon"
else:
    wish="Good Evening"

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak(f"Hello {wish} I am Bot. What is your name")

r=sr.Recognizer()


def start():
    while True:
        query=""
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)
            print("Recognizing...")
            try:
                query=r.recognize_google(audio)
                print(f"User said: {query}")
                speak(f"You said: {query}")
            except:
                print("Sorry I didn't get it")
                continue
        if 'about' in query:
            query=query.replace("about","")
            speak(f'Searching for {query}')
            getresult=wikipedia.summary(query,sentences=1)
            print(getresult)
            speak(getresult)
        elif 'search' in query:
            query=query.replace("search","")
            webbrowser.open(f'https://www.google.com/search?q={query}')
        elif 'play' in query:
            query=query.replace("play","")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
        elif 'current time' in query:
            print(datetime.now())
            speak(datetime.now())
        """elif 'shutdown' and 'computer' in query:
            os.system("shutdown /s /t 2")
        elif 'restart' in query:
            if 'computer' in query:
                os.system("shutdown /r /t 2")"""
with sr.Microphone() as source:
    print("Tell only your name...")
    audio=r.listen(source)
    print("Recognizing...")
    try:
        audioget=r.recognize_google(audio)
        print(f'Hi {audioget}. Please command me what i can do for you')
        speak(f'Hi {audioget}. Please command me what i can do for you')
        start()
    except:
        print("Sorry I didn't get")