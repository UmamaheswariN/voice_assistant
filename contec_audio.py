import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import yagmail

from weather import *
import re
from util import *

listener = sr.Recognizer()
engine = pyttsx3.init()  # used to talk
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # used to change voice



def talk(command):
    engine.say(command)
    engine.runAndWait()


def listen_command():
    global command
    try:
        with sr.Microphone() as source:
            print('Clearing Background Noises...')
            listener.adjust_for_ambient_noise(source, duration=1)
            print('Waiting for your messages ...')
            voice = listener.listen(source)
            print('Done recording')
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        print('except')
    return command


def is_weather_search_action(recognized_text):
    text = recognized_text.lower()  # convert everything to lower case
    return "what is the weather in" in text


def extract_city_name_for_weather_action(recognized_text):
    text = recognized_text.lower()
    return text.replace("what is the weather in", "").strip()


def is_twitter_profile_action(recognized_text):
    pattern = "open up (\S+) on twitter"
    matches = re.findall(pattern, recognized_text, re.IGNORECASE)
    return len(matches) > 0


def get_twitter_profile(recognized_text):
    pattern = "open up (\S+) on twitter"
    matches = re.findall(pattern, recognized_text, re.IGNORECASE)
    return matches[0]


def run_alexa():
    command = listen_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)  # to play command from youtube
        print('playing')
    elif 'email' in command:
        text = format(command)
        receiver = 'muma@gocontec.com'
        message = text
        print(text)
        sender = yagmail.SMTP(user='muma@gocontec.com', password='ukrenee@102013', host='smtp.office365.com',
                              port=587, smtp_starttls=True, smtp_ssl=False)
        sender.send(to=receiver, subject='this is an automated mail', contents=message)
        print('sent mail')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)  # to get time
        print(time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)  # wikipedia about 1 line
        talk(info)
        print(info)
    elif 'name' in command:
        talk('My name is Alexis')
    elif 'are you single' in command:
        talk('am in relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())  # coding joke
        print(pyjokes.get_joke())
    elif 'who is the developer' in command:
        talk('uma')
        print('uma')
    elif is_weather_search_action(command):
        print(command)
        talk(WeatherService().get_weather_data(extract_city_name_for_weather_action(command)))

    elif is_twitter_profile_action(command):
        print(command)
        open_page("https://twitter.com/" + get_twitter_profile(command))
    else:
        talk('Please repeat again.')

    # while True:
    run_alexa()
