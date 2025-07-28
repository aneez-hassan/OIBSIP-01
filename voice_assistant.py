import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

def run_assistant():
    greet()
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! I am your assistant.")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {now}")
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif "exit" in command:
            speak("Goodbye!")
            break

run_assistant()
