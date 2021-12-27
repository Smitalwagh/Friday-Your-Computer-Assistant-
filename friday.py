import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import wolframalpha
import sys
import random


client = wolframalpha.Client('UAEJ72-73P7XULYJV')



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Ma'am!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Smital!")   

    else:
        speak("Good Evening Ma'am!")  

    speak("I am Fryday. How may I Assist you")       

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Your next command Maam")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')#hi-IN  mr-IN
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        #print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        if 1:
            query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'start youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'start google' in query:
            webbrowser.open("google.com")
    
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = "C:\\Users\\smita\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath ="C:\\Friday\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome ' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)

        elif 'email to Smital' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "smitalwagh278@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
           
        elif 'Hello Jarvis' in query:
            speak('Hello Maam')

        elif 'bye' in query:
            speak('Bye Maam, have a good day.')
            sys.exit()

        elif ' ok bye' in query:
            speak('Bye Maam, have a good day.')
            sys.exit()

        elif 'abort' in query:
            speak('Bye Maam, have a good day.')
            sys.exit()

        elif 'stop' in query:
            speak('Bye Maam, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it')
                    speak(results)
                    print(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it')
                    speak('WIKIPEDIA says - ')
                    speak(results)
                    print(results)
            except:
                webbrowser.open('www.google.com')