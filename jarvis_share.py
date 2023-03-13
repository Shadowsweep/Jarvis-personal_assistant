import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell how may i help")
def takeCommand():
    ''' it takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said:",query)   

    except Exception as err:
        # print(err)

        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('youremailgmail.com','your-password')
    server.sendEmail('youremail@gmail.com',to,content)
    server.close()



if __name__=="__main__":
    WishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
# logic for executing task based on Query

        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            # pywhatkit.playonyt(takeCommand())
            
        
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        
        elif 'open pomodoro' in query:
            webbrowser.open("http://pomofocus.io/")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open spotify' in query:
            webbrowser.open("open.spotify.com")
        
       
       
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak("Sir, The time is :",strTime)


        elif 'open code' in query:
            codePath = "Location of your vs code "
            os.startfile(codePath)
        
        
        
       

        elif 'open time table' in query:
            
            tt = "location of your pdf file"
            os.startfile(tt)
        
       

            
            
        elif 'stop' in query:
            exit()


    
  