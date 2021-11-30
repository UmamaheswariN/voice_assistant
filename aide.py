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
import requests, json

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
from tkinter import *
from tkinter.ttk import *

obj = tk.Tk()
obj.title("Contec Voice Assistant")
obj.geometry('800x500')
obj.resizable(False, False)
obj.config(bg='')

import playsound

googlenews = GoogleNews()

listener = sr.Recognizer()  # initialization
engine = pyttsx3.init()  # used to talk
voices = engine.getProperty('voices')
# setter method .[0]=male voice and
# [1]=female voice in set Property.
engine.setProperty('voice', voices[1].id)


def getCorrectPath(relative_path):
    p = os.path.abspath(".").replace('/dist', "")
    return os.path.join(p, relative_path)


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
    talk("confirm your Language by mentioning as follows. English,  Spanish, Tamil, Hindi")
    # talk("Tell me how can I help you?")


def choose_language():
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
            print('Listening')
            voice = listener.listen(source)
            print('Done recording')
            print(voice)
            langCommand = listener.recognize_google(voice)  # Using google to recognize audio
            langCommand = langCommand.lower()
            print(langCommand)
            return langCommand
    except:
        talk("Pardon me, please say that again")
        return "None"


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
            print('Listening')
            voice = listener.listen(source)
            print('Done recording')
            print(voice)
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
            talk('Tell me how can I help you?..')
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


def listen_command_spanish():
    global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.2)
            talk('Dime cómo puedo ayudarte?')
            talk('Dime cómo puedo ayudarte?')
            print('Dime cómo puedo ayudarte?')
            voice = listener.listen(source)
            print('Done recording')
            command = listener.recognize_google(voice, language="es-MX")  # Using google to recognize audio
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


def listen_command_tamil():
    global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.2)
            print('நான் உங்களுக்கு எப்படி உதவ முடியும் என்று சொல்லுங்கள்?')
            voice = listener.listen(source)
            talk('நான் உங்களுக்கு எப்படி உதவ முடியும் என்று சொல்லுங்கள்?')
            voice = 'நான் உங்களுக்கு எப்படி உதவ முடியும் என்று சொல்லுங்கள்?'
            print('Done recording')
            command = listener.recognize_google(voice, language='ta-IN')  # Using google to recognize audio
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


def listen_command_hindi():
    global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.2)
            talk('mujhe batao main tumhaaree kaise madad kar sakata hoon?')
            voice = listener.listen(source)
            print('Done recording')
            command = listener.recognize_google(voice, language='hi-IN')  # Using google to recognize audio
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


def run_alexa(choosenLangcode):
    global command
    print(choosenLangcode)
    talk(choosenLangcode)
    if 'english' in choosenLangcode:
        print('am in english')
        command = listen_command()
    elif 'spanish' in choosenLangcode:
        print('am in spanish')
        command = listen_command_spanish()
    elif 'tamil' in choosenLangcode:
        print('am in tamil')
        command = listen_command_tamil()
    elif 'hindi' in choosenLangcode:
        print('am in hindi')
        command = listen_command_hindi()
    else:
        print('am in default language')
        command = listen_command()

    print(command)
    if is_weather_search_action(command):
        print(command)
        talk(WeatherService().get_weather_data(extract_city_name_for_weather_action(command)))

    elif is_twitter_profile_action(command):
        print(command)
        open_page("https://twitter.com/" + get_twitter_profile(command))

    elif 'bench request' in command or 'issue' in command or 'create ticket' in command:
        talk("Happy to assist you! Can you tell your name")
        requesterName = talk_command()
        print(requesterName)
        if 'None' in requesterName:
            talk("Pardon! Can you tell your name again")
            requesterName = talk_command()
            print(requesterName)
        else:
            talk("Can you tell your stationName ")
            stationName = talk_command()
            print(stationName)
            if 'None' in stationName:
                talk("Pardon! Can you tell your stationName again")
                stationName = talk_command()
                print(stationName)
            else:
                talk("Can you describe issue")
                reqIssueDescription = talk_command()
                print(reqIssueDescription)
                if 'None' in reqIssueDescription:
                    talk("Pardon! Can you describe the issue once again")
                    reqIssueDescription = talk_command()
                    print(reqIssueDescription)
                else:
                    if 'None' in requesterName or 'None' in stationName or 'None' in reqIssueDescription:
                        talk("Pardon! The request not created due to invalid values.Please repeat")
                    else:
                        talk('I am confirming the details as you given')
                        talk('your name')
                        talk(requesterName)
                        talk('your station name')
                        talk(stationName)
                        talk('your issue description')
                        talk(reqIssueDescription)
                        talk('All these details are okay? Shall i proceed to create? please confirm yes or no')
                        confirmCreateRequest = talk_command()
                        if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest:
                            print('BenchRequest Service..')
                            benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                            benchData = {"id": 0, "requestorId": 0, "requesterName": requesterName,
                                         "stationId": 0, "stationName": stationName, "siteId": 1004, "statusId": 3,
                                         "categoryId": 1, "subcategoryId": 1, "assigneeId": 7668, "priority": 0,
                                         "repairAction1Id": 0, "repairAction2Id": 0, "repairAction3Id": 0,
                                         "diagnosisId": 0,
                                         "sBUId": 1, "systemId": 0, "description": reqIssueDescription,
                                         "comments": "test", "userId": 0, "requesterEmail": '',
                                         "supervisorId": 7687, "email": '',
                                         "supervisorName": "CiscoSupervisor", "userfor": "requester",
                                         "status": "Assigned",
                                         "docs": ""}
                            print(benchData)

                            headers = {'Content-type': 'application/json'}
                            print('BenchRequest Service call in progress..')
                            # responeData = requests.put(benchReqUrl, json={'json_payload': data}, headers=headers)
                            responeData = requests.put(benchReqUrl, headers=headers, data=json.dumps(benchData))
                            print(responeData.json())
                            print(responeData)
                            if '<Response [200]>' in responeData:
                                talk('Successfully created your ticket in Bench request. Thanks for using R1.0')
                                stopspeacking()
                            else:
                                talk('Thanks for using R1.0')
                                stopspeacking()
                        elif 'no' in confirmCreateRequest:
                            talk('This issue will not create without your confirmation.')
                            stopspeacking()

    elif 'solicitud de banco' in command or 'asunto' in command:
        print('going to ask ur name in spanish')
        talk("Feliz de ayudarte! Puedes decir tu nombre")
        print('Feliz de ayudarte! Puedes decir tu nombre')
        requesterName = talk_command()
        print(requesterName)
        if 'None' in requesterName:
            talk("¡Perdón! ¿Puedes decir tu nombre de nuevo?")
            requesterName = talk_command()
            print(requesterName)
        else:
            print('going to ask ur stationName in spanish')
            talk("Puedes decir el nombre de tu estación? ")
            print('Feliz de ayudarte! Puedes decir tu nombre')
            stationName = talk_command()
            print(stationName)
            if 'None' in stationName:
                talk("Perdón! Puedes decir el nombre de tu estación?")
                stationName = talk_command()
                print(stationName)
            else:
                talk("¿Puedes describir el problema?")
                reqIssueDescription = talk_command()
                print(reqIssueDescription)
                if 'None' in reqIssueDescription:
                    talk("Perdón! ¿Puedes describir el problema?")
                    reqIssueDescription = talk_command()
                    print(reqIssueDescription)
                else:
                    if 'None' in requesterName or 'None' in stationName or 'None' in reqIssueDescription:
                        talk("Pardon! The request not created due to invalid values.Please repeat")
                    else:
                        talk('I am confirming the details as you given')
                        talk('your name')
                        talk(requesterName)
                        talk('your station name')
                        talk(stationName)
                        talk('your issue description')
                        talk(reqIssueDescription)
                        talk('All these details are okay? Shall i proceed to create? please confirm yes or no')
                        confirmCreateRequest = talk_command()
                        if 'sí' in confirmCreateRequest or 'se' in confirmCreateRequest or 'z' in confirmCreateRequest:
                            print('BenchRequest Service..')
                            benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                            benchData = {"id": 0, "requestorId": 0, "requesterName": requesterName,
                                         "stationId": 0, "stationName": stationName, "siteId": 1004, "statusId": 3,
                                         "categoryId": 1, "subcategoryId": 1, "assigneeId": 7668, "priority": 0,
                                         "repairAction1Id": 0, "repairAction2Id": 0, "repairAction3Id": 0,
                                         "diagnosisId": 0,
                                         "sBUId": 1, "systemId": 0, "description": reqIssueDescription,
                                         "comments": "test", "userId": 0, "requesterEmail": '',
                                         "supervisorId": 7687, "email": '',
                                         "supervisorName": "CiscoSupervisor", "userfor": "requester",
                                         "status": "Assigned",
                                         "docs": ""}
                            print(benchData)

                            headers = {'Content-type': 'application/json'}
                            print('BenchRequest Service call in progress..')
                            # responeData = requests.put(benchReqUrl, json={'json_payload': data}, headers=headers)
                            responeData = requests.put(benchReqUrl, headers=headers, data=json.dumps(benchData))
                            print(responeData.json())
                            print(responeData)
                            if '<Response [200]>' in responeData:
                                talk('Successfully created your ticket in Bench request. Thanks for using R1.0')
                                stopspeacking()
                            else:
                                talk('Thanks for using R1.0')
                                stopspeacking()
                        elif 'no' in confirmCreateRequest:
                            talk('This issue will not create without your confirmation.')
                            stopspeacking()


    elif 'powerpoint' in command or 'presentation' in command:
        talk("opening Power Point presentation")
        power = r"C:\Users\muma\Desktop\Python_Learning_stuffs\Our Own Virtual Assistant.pptx"
        os.startfile(power)
        # file = "demo_audio_test.m4a"
        # file = "my_audio_presentation_final.m4a"
        # os.startfile(file)
        sys.exit()
        # time.sleep(105)

    elif "write a note" in command:
        talk("ready to take notes...")
        note = talk_command()
        file = open('demotext.txt', 'w')
        file.write(note)
        talk("The text file ready now with your notes")
        # snfm = talk_command()
        # if 'yes' in snfm or 'sure' in snfm:
        # strTime = datetime.datetime.now().strftime('%I:%M %p')
        # file.write(strTime)
        # file.write(" :- ")
        # file.write(note)
        # else:
        # file.write(note)
        # talk("The text file ready now")

    elif "open note" in command:
        talk("Opening Notes")
        file = open("demotext.txt", "r")
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

    elif 'company' in command:
        webbrowser.open_new_tab("https://www.gocontec.com/")
        talk("Your company website is open now")
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
        # talk('Please repeat again.')
        return 0


def startspeakeithme():
    wishMe()
    choosenLangcode = choose_language()
    talk(choosenLangcode)
    # time.sleep()
    while True:
        run_alexa(choosenLangcode)


def stopspeacking():
    talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    sys.exit()


#   subprocess.call(["sleep", "/l"])

if __name__ == '__main__':
    canvas = Canvas(
        obj,
        bg="#E7EBEE",
        height=500,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    bg = PhotoImage(file=getCorrectPath("assets/bga.png"))

    canvas.pack(fill="both", expand=True)

    # Display image
    canvas.create_image(0, 0, image=bg,
                        anchor="nw")

    button_image_1 = PhotoImage(
        file=getCorrectPath("assets/mic.png"))
    button_1 = tk.Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=startspeakeithme,
        relief="flat", cursor="hand1"
    )
    button_1.place(
        x=329.0,
        y=122.0,
        width=132.0,
        height=128.0
    )

    button_image_2 = PhotoImage(
        file=getCorrectPath("assets/logo.png"))
    button_2 = tk.Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat", cursor="hand1"
    )
    button_2.place(
        x=23.0,
        y=10.0,
        width=108.0,
        height=103.0
    )

    button_image_3 = PhotoImage(
        file=getCorrectPath("assets/quit.png"))
    button_3 = tk.Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=stopspeacking,
        relief="flat", cursor="hand1"
    )
    button_3.place(
        x=334.0,
        y=260.0,
        width=145.0,
        height=50.0
    )
    img = tk.Image("photo", file=getCorrectPath("assets/inc.png"))
    obj.tk.call('wm', 'iconphoto', obj._w, img)
    # obj.config(menu="")
    obj.mainloop()

# wishMe()
# time.sleep(1)
# while True:
# run_alexa()
