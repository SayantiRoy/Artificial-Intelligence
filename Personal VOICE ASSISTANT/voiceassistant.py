import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #1-Female voice
recognizer=sr.Recognizer()

def logic():
    with sr.Microphone() as source:
        print('Clearing Background noises.....Please Wait!')
        recognizer.energy_threshold=4000
        print('How can I help you ?.....')
        recordedaudio=recognizer.listen(source)
    
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
    if 'hai' in text:
        a = 'Hi! This is your Personal assistant! How can i help you?'
        engine.say(a)
        engine.runAndWait()
    if 'chrome' in text:
        a = 'Opening Chrome...'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  
        subprocess.Popen([programName])
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        engine.say(time)
        engine.runAndWait()  
    if 'play' in text:
        a = 'Playing in youtube...'
        engine.say(a)
        engine.runAndWait()  
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b = 'Opening Youtube...'
        engine.say(b) 
        engine.runAndWait()
        webbrowser.open('www.youtube.com') 
        engine.runAndWait()   
    if 'google' in text:
        a = 'Opening Google...'
        engine.say(a)
        engine.runAndWait() 
        webbrowser.open('www.google.com')
        engine.runAndWait()      
    if 'amazon' in text:
        a = 'Opening Amazon...'
        engine.say(a)
        engine.runAndWait() 
        webbrowser.open('www.amazon.in')
        engine.runAndWait()       
    if 'github' in text:
        a = 'Opening Github...'
        engine.say(a)
        engine.runAndWait() 
        webbrowser.open('https://github.com/')      
    if 'whatsapp' in text:
        a = 'Opening Whatsapp web...'
        engine.say(a)
        engine.runAndWait() 
        webbrowser.open('https://web.whatsapp.com/')         
while True:
    logic() 