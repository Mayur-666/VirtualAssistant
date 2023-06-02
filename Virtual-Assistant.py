import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
engine.setProperty('voice','english+f4')
#voices = engine.getProperty("voices")
#engine.setProperty("voices",voices[0].id)   #change it to 2 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis , How can i help you ?")

def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..............")
        r.pause_threshold = 1              #change it to 2
        audio = r.listen(source)

        try:
            print("Recognizing..........")
            query = r.recognize_google(audio,language="en-in")
            print(f"USer said : {query}\n")
        
        except Exception as e:
            speak("Oh Say that again please.....")
            return "None"
        return query

if __name__=="__main__":
    greet()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia........")
            query = query.replace("wikipedia"," ")
            results= wikipedia.summary(query,sentence=2)  #change it to 2
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'stop' in query:
            speak("Goodbye and see you again! ")
            exit()
