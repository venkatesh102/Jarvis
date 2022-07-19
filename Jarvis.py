import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki
import pyjokes
import os
import webbrowser
import time

listener = sr.Recognizer()

speaker = pyttsx3.init()
""" RATE"""
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)

"""VOLUME"""
volume = speaker.getProperty('volume')
speaker.setProperty('volume',1.1)
"""VOICE"""
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()
va_name= 'jarvis'
speak('I am your'+va_name + ':Tell me boss')
def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print('Listening......')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if va_name in command:
                command=command.replace(va_name + ' ','')

    except:
        print('Check your microphone')
    return command
while True:
    user_command=take_command()
    print(user_command)
    if 'close' in user_command:
        print('see you again boss')
        speak('see you again boss')
        break
    elif 'time' in user_command:
        cur_time=dt.datetime.now().strftime('%I:%M:%p')
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command=user_command.replace('play','')
        print('playing'+ user_command)
        speak('playing'+user_command)
        pk.playonyt(user_command)
    elif 'search' in user_command or 'google'in user_command:
        user_command=user_command.replace('search','')
        user_command = user_command.replace('google', '')
        speak('searching for'+user_command)
        print('searching for'+user_command)
        pk.search(user_command)
    elif 'youtube' in user_command:
        webbrowser.open('https://www.youtube.com')
        print('opening youtube')
        speak('opening youtube')
    elif 'gmail' in user_command or 'email' in user_command :
        webbrowser.open('https://mail.google.com/mail/u/0/?ogbl#inbox')
        print('opening gmail')
        speak('opening gmail')
    elif 'google classroom' in user_command:
        webbrowser.open('')
        print('opening classroom')
        speak('opening classroom')
    elif 'who is' in user_command or 'what is' in user_command:
        user_command=user_command.replace('who is','')
        info=wiki.summary(user_command,5)
        print(info)
        speak(info)
    elif 'who are you' in user_command or 'your name' in user_command:
        speak('I am your' + va_name + ':Tell me boss')
    elif 'old are you' in user_command or 'your age' in user_command:
        print('I am a robot so i dont have exact age ')
        speak('I am a robot so i dont have exact age')

    elif 'how are you' in user_command:
        reply='i am fine You are very kind to ask, especially in these tempestuous times' or 'i am splendid!Thank you for asking'
        print(reply)
        speak(reply)
    elif 'are you single' in user_command:
        an="i'm happy to say i feel whole all on my own"
        print(an)
        speak(an)
    elif 'about you' in user_command:
        info='i am a Voice Based AI Assistant which is developed in Python Programming Language, i uses Different Technologies To Add New Unique Features and can Automate Tasks with just One Voice Command,i am a Desktop Based AI Assistant '
        print(info)
        speak(info)
    elif 'joke' in user_command:
        joke1=pyjokes.get_joke(language="en",category="all")
        print(joke1)
        speak(joke1)
    elif 'notepad' in user_command:
        user_command = user_command.replace('open', '')
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Notepad.lnk")
        print('opening notepad')
        speak('opening notepad')
    elif 'downloads' in user_command:
        os.startfile("C:\\Users\\USER\Downloads")
        print('opening downloads')
        speak('opening downloads')
    else:
        speak('sorry boss i cant understand you ' + 'please say it again')
        break
    else:
        speak('sorry boss i cant understand you '+'please say it again')
    time.sleep(5)