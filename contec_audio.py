import speech_recognition as sr  # used to convert human speech to text
import pyttsx3  # used to convert text to speech
import pywhatkit  # to play you tube music
import datetime
import wikipedia
import pyjokes
import time
import os
import subprocess
from GoogleNews import GoogleNews
import sys  # to get exit
import imdb  # to get any movie details
from PIL import ImageTk
import osascript

from weather import *
import re
from util import *
# importing required module
import tkinter as tk
from tkinter.ttk import *
# import messagebox from tkinter module
import tkinter.messagebox
from tkinter import LEFT, RIGHT, TOP, BOTTOM, CENTER
from tkinter.font import Font

obj = tk.Tk()
obj.title("Contec Voice Assistant")
obj.geometry('500x300')
obj.resizable(True, True)
obj.config(bg='yellow')

import playsound

googlenews = GoogleNews()

listener = sr.Recognizer()  # initialization
engine = pyttsx3.init()  # used to talk
voices = engine.getProperty('voices')
# setter method .[0]=male voice and
# [1]=female voice in set Property.
engine.setProperty('voice', voices[1].id)


def talk(command):
    # Method for the speaking of the the assistant
    engine.say(command)
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")
    assname = ("R 1 point 0")
    talk("Loading your personal assistant")
    talk(assname)
    #talk("Tell me how can I help you?")


def talk_command():
    global command
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.5)
            # talk('Ask me anything')
            voice = listener.listen(source)
            print('Done recording')
            command = listener.recognize_google(voice)  # Using google to recognize audio

            command = command.lower()
    except:
        talk("Pardon me, please say that again")
        return "None"
    return command


def listen_command():
    global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.2)
            talk('Ask me anything..')
            voice = listener.listen(source)
            print('Done recording')
            command = listener.recognize_google(voice)  # Using google to recognize audio
            command = command.lower()
            if 'R 1 point 0' in command:
                command = command.replace('R 1 point 0', '')
            if "good bye" in command or "ok bye" in command or "bye" in command:
                talk('your personal assistant R-one is shutting down,Good bye')
                print('your personal assistant R-one is shutting down,Good bye')
                time.sleep(30)
                sys.exit()
    except:
        talk("Pardon me, please say that again")
        return "None"
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
    print(command)
    if is_weather_search_action(command):
        print(command)
        talk(WeatherService().get_weather_data(extract_city_name_for_weather_action(command)))

    elif is_twitter_profile_action(command):
        print(command)
        open_page("https://twitter.com/" + get_twitter_profile(command))

    elif 'powerpoint' in command or 'presentation' in command:
        talk("opening Power Point presentation")
        power = r"C:\Users\muma\Desktop\Python_Learning_stuffs\Our Own Virtual Assistant.pptx"
        os.startfile(power)
        # file = "demo_audio_test.m4a"
        file = "my_audio_presentation_final.m4a"
        os.startfile(file)
        time.sleep(105)

    elif "write a note" in command:
        talk("Am ready to write...")
        note = talk_command()
        file = open('demotext.txt', 'w')
        talk("Should i include date and time")
        snfm = talk_command()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
        talk("The text file ready now")

    elif "show note" in command:
        talk("Showing Notes")
        file = open("demonote.txt", "r")
        print(file.read())
        talk(file.read(6))

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)  # to play command from youtube
        print('playing')
        time.sleep(10)

    elif 'time' in command:
        timenow = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + timenow)  # to get time
        print(timenow)
        time.sleep(1)

    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)  # wikipedia about 1 line
        talk("According to Wikipedia")
        talk(info)
        print(info)
        time.sleep(1)

    elif 'open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        talk("youtube is open now")
        time.sleep(5)

    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in command:
        webbrowser.open_new_tab("gmail.com")
        talk("Google Mail open now")
        time.sleep(5)

    elif "open stackoverflow" in command:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        talk("Here is stackoverflow")
        time.sleep(5)

    elif 'news' in command:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif 'search' in command:
        searchtxt = command.replace("search", "")
        webbrowser.open_new_tab(searchtxt)
        time.sleep(5)

    elif 'who are you' in command or 'what can you do' in command:
        talk('I am R-one version 1 point 0 your personal assistant.'
             'I am programmed to minor tasks like'
             'opening youtube, google '
             'chrome, gmail,'
             'stackoverflow ,predict time,take a photo,'
             'search wikipedia,predict weather'
             'In different cities, get top headline news from times of india '
             'and you can ask me computational or geographical questions too!')
        print('I am R-one version 1 point 0 your personal assistant.'
              'I am programmed to minor tasks like'
              'opening youtube, google '
              'chrome, gmail,'
              'stackoverflow ,predict time,take a photo,'
              'search wikipedia,predict weather'
              'In different cities, get top headline news from times of india '
              'and you can ask me computational or geographical questions too!')
        time.sleep(2)

    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
        talk("I was built by U")
        print("I was built by U")

    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you")

    elif 'movie' in command:
        talk('Say the movie name')
        # gathering information from IMDb
        moviesdb = imdb.IMDb()

        # search for title
        text = listen_command()

        # passing input for searching movie
        movies = moviesdb.search_movie(text)

        talk("Searching for " + text)
        if len(movies) == 0:
            talk("No result found")
        else:

            talk("I found these:")

            for movie in movies:

                title = movie['title']
                year = movie['year']
                # speaking title with releasing year
                talk(f'{title}-{year}')

                info = movie.getID()
                movie = moviesdb.get_movie(info)

                title = movie['title']
                year = movie['year']
                rating = movie['rating']
                # plot = movie['plot outline']

                # the below if-else is for past and future release
                if year < int(datetime.datetime.now().strftime("%Y")):
                    talk(
                        f'{title}was released in {year} has IMDB rating of {rating}.')
                    print(
                        f'{title}was released in {year} has IMDB rating of {rating}.')
                    break

                else:
                    talk(
                        f'{title}will release in {year} has IMDB rating of {rating}.')
                    print(
                        f'{title}will release in {year} has IMDB rating of {rating}.')
                    break

    elif 'joke' in command:
        talk(pyjokes.get_joke())  # coding joke
        print(pyjokes.get_joke())
        time.sleep(1)

    elif 'launch' in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname + ".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            talk('I have launched the desired application')

    elif "log off" in command or "sign out" in command or "log out" in command or "stop" in command:
        talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        sys.exit()
    #   subprocess.call(["sleep", "/l"])

    elif 'headlines' in command:
        engine.say('Getting headlines for you ')
        engine.runAndWait()
        googlenews.get_news('Today news')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')

    elif 'tech' in command:
        engine.say('Getting tech for you ')
        engine.runAndWait()
        googlenews.get_news('Tech')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')

    elif 'politics' in command:
        engine.say('Getting politics for you ')
        engine.runAndWait()
        googlenews.get_news('Politics')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')

    elif 'sports' in command:
        engine.say('Getting sports for you ')
        engine.runAndWait()
        googlenews.get_news('Sports')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')

    elif 'cricket' in command:
        engine.say('Getting cricket for you ')
        engine.runAndWait()
        googlenews.get_news('cricket')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')

    else:
        #talk('Please repeat again.')
        return 0


def startspeakeithme():
    wishMe()
    # time.sleep()
    while True:
        run_alexa()


def stopspeacking():
    talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    sys.exit()


#   subprocess.call(["sleep", "/l"])

if __name__ == '__main__':
    msg = tk.Label()
    msg.grid(row=0, column=0)
    img = tk.PhotoImage(file="R1_image.png")
    label = tk.Label(obj, image=img)
    label.place(x=0, y=0)
    fontStyle = Font(family="Lucida Grande", size=20)

    btn = tk.Button(text="Speak With R-1.0", width=15,
                    height=2, font=fontStyle,
                    compound=LEFT, command=startspeakeithme)
    # btn.place(x=20, y=50)
    btn.grid(row=1, column=3, padx=100)
    btn.config(bg="green")

    btn1 = tk.Button(text="Stop", width=15,
                     height=2, font=fontStyle,
                     compound=CENTER, command=stopspeacking)

    # btn1.place(x=250, y=50)
    btn1.grid(row=1, column=5, padx=100)
    btn1.config(bg="yellow")

    btn2 = tk.Button(text='Quit !', width=15,
                     height=2, font=fontStyle,
                     compound=RIGHT, command=obj.destroy)
    # btn2.place(x=700, y=50)
    btn2.grid(row=1, column=8, padx=100)
    btn2.config(bg="red")

    obj.mainloop()

# wishMe()
# time.sleep(1)
# while True:
# run_alexa()
