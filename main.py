# Last Update 4/11/2021 14:20
#                           by Dionisis Giannaropoulos
import pyttsx3
import os
import platform
import speech_recognition as sr

if platform.system()=='Windows':
    engine_init = 'sapi5'
    engine_init_number = 1
elif platform.system()=='Linux':
    engine_init = 'espeak'
    engine_init_number = 10

def engine_say(text):
      
    engine = pyttsx3.init(engine_init)

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[engine_init_number].id)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1)  
    
    engine.say(text)  
      
    engine.runAndWait()

def get_audio():
  
    rObject = sr.Recognizer()
    audio = ''
  
    with sr.Microphone() as source:
        print("Speak...")
          
       
        audio = rObject.listen(source, phrase_time_limit = 5) 
    print("Stop.") # limit 5 secs
  
    try:
  
        text = rObject.recognize_google(audio, language ='en-US')
        print("You : ", text)
        return text
  
    except:
  
        engine_say("Could not understand your audio, Please try again !")
        return 0

if __name__ == "__main__":
    engine_say("What's your name, Human?")
    name ='Human'
    name = get_audio()
    engine_say("Hello, " + name + '.')
      
    while(1):
  
        engine_say("What can i do for you?")
        text = get_audio().lower()
  
        if text == 0:
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            engine_say("Ok bye, "+ name+'.')
            break
  
        
        engine_say(text)

