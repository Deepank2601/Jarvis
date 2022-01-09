import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechrecognition
import datetime # pip install datetime
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
import os # pip install os
import smtplib # pip install smtplib

print("Initializing Jarvis")
MASTER="Deepank"

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    print(hour)

    if hour>=0 and hour<12:
        speak("GoodMorning" + MASTER)
    
    elif  hour>=12 and hour<18:
          speak("Good Afternoon" + MASTER)
    
    else:
          speak("Goodnight" + MASTER)
    
    # speak("Hello, I am jarvis! How May I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.listen(source)
    
    try :
        print("Recognizing....")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again Please")
        query=None
    
    return query

wishMe()
query=takeCommand()
speak("Initializing Jarvis")

if 'wikipedia' in query.lower():
    speak("Searching Wikipedia...")
    query=query.replace('wikipedia',"")
    result=wikipedia.summary(query,sentences=2)
    #speak(result)
    print(result)

elif 'open youtube' in query.lower():
    url="Yotube.com"
    chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe%s"
    webbrowser.get(chromepath).open(url)

elif 'open google' in query.lower():
    url="google.com"
    chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe%s"
    webbrowser.get(chromepath).open(url)

elif 'play music' in query.lower():
    songs_dir="C:\\Users\\ACER\\Music\\Video Projects"
    songs=os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir,songs[1]))

elif 'the time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M:%S:")
    speak(f" {MASTER} The time is {strTime}")

elif 'open the code' in query.lower():
    path="C:\\Users\\ACER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
    os.startfile(path)
