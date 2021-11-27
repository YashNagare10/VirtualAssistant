import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import emailData

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

name = input("Enter your name : ")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hr = int(datetime.datetime.now().hour)
    if (hr >=0 and hr < 12):
        speak("Good Morning"+name+"how can i help you")
    elif (hr >= 12 and hr < 18):
        speak("Good Afternoon"+name+"how can i help you")
    else:
        speak("Good Evening"+name+"how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language = 'en-in')
            print("User said : "+query)
        except Exception as e:
            print("Say that again please")
            return "None"
        return query

def sendEmail(sender, reciever, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender["username"], sender["password"])
    server.sendmail(sender["username"], reciever, content)
    server.close()

if __name__ == "__main__":
    greet()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google.com")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open vs code' in query:
            os.startfile("C:\\Users\\Yash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'open vlc' in query:
            os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is "+strtime)
        elif 'send email to yash' in query:
            try:
                speak("what should i send")
                content = takeCommand()
                sender = emailData.sender[1]
                reciever = emailData.reciever["yash"]
                speak("sending email to yash")
                sendEmail(sender, reciever, content)
                speak("email sent successfully")
            except Exception as e:
                print(e)
                speak("i am sory")
                speak("i am not able to send this email")