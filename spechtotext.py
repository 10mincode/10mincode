import speech_recognition as sr

r=sr.Recognizer()


def stot(r):
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("recognizing...")

        try:
            print(r.recognize_google(audio))
        except:
            print("I haven't reconized")
            stot(r)
stot(r)


