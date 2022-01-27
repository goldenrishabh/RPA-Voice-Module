import os
import subprocess
import time
import playsound
import sys
import speech_recognition as sr
from gtts import gTTS

# stderr = open("Speechlogfile.txt",'a')
# sys.stderr = stderr

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def todo(text):
    if "add" in text.split()[0]:
        text = text.replace("add ","")
        text = text.replace("to my todo list ","")
        text = text.replace("in my todo list ","")
        text = text.replace("to the todo list that i ","")
        text = text.replace("that ","")
        text = text.replace("i have to ","")
        text = text.replace("my ","")
        text = text.replace("i ","")
        text = text.replace("also ","")
        text = text.replace("to","")
        text = text.replace("list","")
        text = text.replace("do ","")
        list_file = open('todo.txt', "a")
        list_file.write(f"{text} \n")
        speak(f"i have added {text} in your todo list ")
        print(f"Added todo :{text} ")
    
    elif "list" in text:
        list_file = open('todo.txt', "r")
        list_file.seek(0)
        speak("you have")
        for task in list_file.readlines():
            speak(task)   

         

def care(text):
    speak("I am doing great! Thanks for asking!")
    speak("What about you?")
    text = get_audio()

    if "not" not in text:
        if  "awesome" in text or "nice" in text or "good" in text or "great" in text:
            speak("Thats good to hear!")
    

    elif "not" or "bad" or "poor" or "don't" in text:
        speak("Why is that? stay cheerful!")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception"+str(e))

    return said.lower()







wakeCommand = "hey buddy"
while True:

    text = get_audio()

    if text.count(wakeCommand)>0: 
        existence = True
        speak("hello sir!")
        while(existence == True):
            text = get_audio()
            if "add" in text or "list" in text or "task" in text:
                todo(text)
            if "how are you" in text or "what's up" in text:
                care()
            



