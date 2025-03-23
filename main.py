import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 
import requests
recognizer = sr.Recognizer()
engine = pyttsx3.init()




def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


    '''elif "okay" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=apiKey
            data = r.json()

            articles = data.get('articles',[])

            for article in articles:
                speak(article['title'])'''
    
                  

if __name__ == '__main__':
    speak("I am On...")
    while True:
        
        r = sr.Recognizer()
        
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))
