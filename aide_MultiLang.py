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
import gtts as gt
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
from gtts import gTTS
import random
from googletrans import Translator
import googletrans
import json
import keyboard
from fedex.tools.conversion import sobject_to_json

obj = tk.Tk()
obj.title("Contec Voice Assistant")
obj.geometry('800x500')
obj.resizable(False, False)
obj.config(bg='')

import playsound

googlenews = GoogleNews()
translator = Translator()

listener = sr.Recognizer()  # initialization
engine = pyttsx3.init()  # used to talk


def getCorrectPath(relative_path):
    p = os.path.abspath(".").replace('/dist', "")
    return os.path.join(p, relative_path)


def talk(command):
    engine = pyttsx3.init()  # used to talk
    voices = engine.getProperty('voices')
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[1].id)
    # Method for the speaking of the the assistant
    engine.say(command)
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.9)
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
    talk("confirm your Language by mentioning as follows. English,  Spanish, French, Tamil, Hindi")
    # talk("Tell me how can I help you?")


def choose_language():
    print('language function gets called')
    global command
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.5)
            print('Listening')
            voice = listener.listen(source)
            print('Done recording')
            langCommand = listener.recognize_google(voice)  # Using google to recognize audio
            langCommand = langCommand.lower()
            print(langCommand)
            print(listener.recognize_google(voice))
            return langCommand
    except:
        # talk("Pardon me, please say that again")
        audio_string = "Pardon me, please continue from again"
        print(audio_string)
        startspeakeithme()
        # destini_lang = convert_language(audio_string, choosenLangCode)
        # print('translated text')
        # print(destini_lang)
        # return destini_lang
        # return "None"


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
            if "spanish" in choosenLangCode:
                command = listener.recognize_google(voice, language="es-MX")  # Using google to recognize audio
            elif "french" in choosenLangCode:
                command = listener.recognize_google(voice, language="fr-CA")  # Using google to recognize audio
            elif "tamil" in choosenLangCode or "Tamil" in choosenLangCode:
                command = listener.recognize_google(voice, language="ta-IN")  # Using google to recognize audio
            elif "hindi" in choosenLangCode:
                command = listener.recognize_google(voice, language="hi-IN")  # Using google to recognize audio
            else:
                command = listener.recognize_google(voice)  # Using google to recognize audio
                # command = listener.recognize_google(voice, language="en-US")  # Using google to recognize audio
            command = command.lower()
            return command
    except:
        # talk("Pardon me, please say that again")
        audio_string = "Pardon me, please say that again"
        print(audio_string)
        # destini_lang = convert_language(audio_string)
        # print('translated text')
        # print(destini_lang)
        talk(audio_string)
        run_alexa(choosenLangCode)
        return "None"


def multi_talk_command():
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
            command = listener.recognize_google(voice, language="en-US")  # Using google to recognize audio
            """
            if "spanish" in choosenLangCode:
                command = listener.recognize_google(voice, language="es-MX")  # Using google to recognize audio
            elif "french" in choosenLangCode:
                command = listener.recognize_google(voice, language="fr-CA")  # Using google to recognize audio
            elif "tamil" in choosenLangCode:
                command = listener.recognize_google(voice, language="ta-IN")  # Using google to recognize audio
            elif "hindi" in choosenLangCode:
                command = listener.recognize_google(voice, language="hi-IN")  # Using google to recognize audio
            else:
            """
            # command = listener.recognize_google(voice)  # Using google to recognize audio
            # command = listener.recognize_google(voice, language="en-US")  # Using google to recognize audio
            command = command.lower()
            return command
    except:
        # talk("Pardon me, please say that again")
        audio_string = "Pardon me, please say that again"
        print(audio_string)
        # destini_lang = convert_language(audio_string, choosenLangCode)
        # print('translated text')
        talk(audio_string)
        multi_talk_command()
        # return "None"


def multi_talk_command_tamil(choosenLangCode):
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
            # command = listener.recognize_google(voice,  language="ta-IN")

            if "spanish" in choosenLangCode:
                command = listener.recognize_google(voice, language="es-MX")
            elif "french" in choosenLangCode:
                command = listener.recognize_google(voice, language="fr-CA")
            elif "tamil" in choosenLangCode:
                command = listener.recognize_google(voice, language="ta-IN")
            elif "hindi" in choosenLangCode:
                command = listener.recognize_google(voice, language="hi-IN")
            else:
                command = listener.recognize_google(voice, language="en-US")
            # command = listener.recognize_google(voice)
            # command = listener.recognize_google(voice, language="en-US")
            # command = command.lower()
            return command
    except:
        # talk("Pardon me, please say that again")
        audio_string = "Pardon me, please say that again"
        print(audio_string)
        # destini_lang = convert_language(audio_string, choosenLangCode)
        # print('translated text')
        talk(audio_string)
        multi_talk_command()
        # return "None"


def listen_command(choosenLangCode):
    global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.2)
            # talk('Tell me how can I help you?..')
            audio_string = "Tell me how can I help you?"
            print(audio_string)
            destini_lang = convert_language(audio_string, choosenLangCode)
            print('translated text')
            print(destini_lang)
            talk(destini_lang)
            print('listening...')
            voice = listener.listen(source)
            print('Done recording')
            if "spanish" in choosenLangCode:
                command = listener.recognize_google(voice, language="es-MX")  # Using google to recognize audio
            elif "french" in choosenLangCode:
                command = listener.recognize_google(voice, language="fr-CA")  # Using google to recognize audio
            elif "tamil" in choosenLangCode:
                command = listener.recognize_google(voice, language="ta-IN")  # Using google to recognize audio
            elif "hindi" in choosenLangCode:
                command = listener.recognize_google(voice, language="hi-IN")  # Using google to recognize audio
            else:
                command = listener.recognize_google(voice)  # Using google to recognize audio
                # command = listener.recognize_google(voice, language="en-US")  # Using google to recognize audio
            command = command.lower()
            if 'R 1 point 0' in command:
                command = command.replace('R 1 point 0', '')
            if "good bye" in command or "ok bye" in command or "bye" in command:
                talk('your personal assistant R-one is shutting down,Good bye')
                print('your personal assistant R-one is shutting down,Good bye')
                time.sleep(30)
                sys.exit()
        return command
    except:
        # talk("Pardon me, please say that again")
        audio_string = "Pardon me, please say that again"
        print(audio_string)
        destini_lang = convert_language(audio_string, choosenLangCode)
        print('translated text')
        print(destini_lang)
        talk(destini_lang)
        run_alexa(choosenLangCode)
        return "None"


def listen_trac_command():
    global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises...Please wait")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=0.2)
            # talk('Tell me how can I help you?..')
            audio_string = "am ready to take your input?"
            print(audio_string)
            talk(audio_string)
            print('listening...')
            voice = listener.listen(source)
            print('Done recording')
            command = listener.recognize_google(voice, language="en-US")  # Using google to recognize audio
            command = command.lower()
            if 'R 1 point 0' in command:
                command = command.replace('R 1 point 0', '')
            if "good bye" in command or "ok bye" in command or "bye" in command:
                talk('your personal assistant R-one is shutting down,Good bye')
                print('your personal assistant R-one is shutting down,Good bye')
                time.sleep(30)
                sys.exit()
        return command
    except:
        # talk("Pardon me, please say that again")
        audio_string = "Pardon me, please say that again"
        print(audio_string)
        talk(audio_string)
        run_alexa("english")
        return "None"


def is_weather_search_action(recognized_text):
    text = recognized_text.lower()  # convert everything to lower case
    return "what is the weather in" in text


def extract_city_name_for_weather_action(recognized_text):
    text = recognized_text.lower()
    return text.replace("what is the weather in", "").strip()


def run_alexa(choosenLangCode):
    global command
    command = listen_command(choosenLangCode)
    print(command)

    if is_weather_search_action(command):
        print(command)
        talk(WeatherService().get_weather_data(extract_city_name_for_weather_action(command)))
        # museebat or anurodh banaen hindi prounciation
        # problema spanish prounciation
        # problème french

    elif there_exists(["bench request", "issue", "create ticket", "solicitud de banco", "asunto", "asanthu", "assunto",
                       "Crear Ticket", "problème", "problem", "demande de banc", "créer un billet", "பிரச்சனை",
                       "டிக்கெட்", "टिकट", "tikat", "கோரிக்கை", "பெஞ்ச் கோரிக்கை", "मुसीबत", "demande"]):
        audio_string = "Happy to assist you! Can you tell your name"
        print(audio_string)
        if 'spanish' in choosenLangCode or 'french' in choosenLangCode or 'english' in choosenLangCode:
            destini_lang0 = convert_language(audio_string, choosenLangCode)
            talk(destini_lang0)
            print(destini_lang0)
            requesterName = multi_talk_command()
            if 'None' in requesterName:
                audio_string1 = "Pardon! Can you tell your name again"
                print(audio_string1)
                destini_lang110 = convert_language(audio_string1, choosenLangCode)
                print(destini_lang110)
                talk(destini_lang110)
                requesterName = multi_talk_command()
                print(requesterName)
            else:
                audio_string2 = "Can you tell your stationName"
                print(audio_string2)
                destini_lang2 = convert_language(audio_string2, choosenLangCode)
                print(destini_lang2)
                talk(destini_lang2)
                stationName = multi_talk_command()
                print(stationName)
                if 'None' in stationName:
                    audio_string3 = "Pardon! Can you tell your stationName again"
                    print(audio_string3)
                    destini_lang3 = convert_language(audio_string3, choosenLangCode)
                    print(destini_lang3)
                    talk(destini_lang3)
                    stationName = multi_talk_command()
                    print(stationName)
                else:
                    audio_string4 = "Can you describe issue"
                    print(audio_string4)
                    destini_lang4 = convert_language(audio_string4, choosenLangCode)
                    print(destini_lang4)
                    talk(destini_lang4)
                    reqIssueDescription = multi_talk_command()
                    print(reqIssueDescription)
                    if 'None' in reqIssueDescription:
                        audio_string5 = "Pardon! Can you describe the issue once again"
                        print(audio_string5)
                        destini_lang5 = convert_language(audio_string5, choosenLangCode)
                        print(destini_lang5)
                        talk(destini_lang5)
                        reqIssueDescription = multi_talk_command()
                        print(reqIssueDescription)
                    else:
                        if 'None' in requesterName or 'None' in stationName or 'None' in reqIssueDescription:
                            audio_string6 = "Pardon! The request not created due to invalid values.Please repeat"
                            print(audio_string6)
                            destini_lang6 = convert_language(audio_string6, choosenLangCode)
                            print(destini_lang6)
                            talk(destini_lang6)
                        else:
                            audio_string7 = "I am confirming the details as you given"
                            print(audio_string7)
                            destini_lang7 = convert_language(audio_string7, choosenLangCode)
                            talk(destini_lang7)
                            audio_string8 = "your name"
                            print(audio_string8)
                            print(requesterName)
                            destini_lang8 = convert_language(audio_string8, choosenLangCode)
                            print(destini_lang8)
                            talk(destini_lang8)
                            talk(requesterName)
                            audio_string9 = "your station name"
                            print(audio_string9)
                            destini_lang9 = convert_language(audio_string9, choosenLangCode)
                            print(destini_lang9)
                            talk(destini_lang9)
                            talk(stationName)
                            print(stationName)
                            audio_string10 = "your issue description"
                            print(audio_string10)
                            destini_lang10 = convert_language(audio_string10, choosenLangCode)
                            print(destini_lang10)
                            talk(destini_lang10)
                            talk(reqIssueDescription)
                            print(reqIssueDescription)
                            audio_string11 = "All these details are okay? Shall i proceed to create? please confirm yes or no"
                            print(audio_string11)
                            destini_lang11 = convert_language(audio_string11, choosenLangCode)
                            print(destini_lang11)
                            talk(destini_lang11)
                            confirmCreateRequest = multi_talk_command()
                            if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest or 'zee' in confirmCreateRequest or 'ss' in confirmCreateRequest or 'sí' in confirmCreateRequest or 'Oui' in confirmCreateRequest:
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
                                    audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                    print(audio_string12)
                                    destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                    talk(destini_lang12)
                                    print(destini_lang12)
                                    stopspeacking()
                                else:
                                    audio_string13 = 'Thanks for using R1.0'
                                    print(audio_string13)
                                    destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                    talk(destini_lang13)
                                    print(destini_lang13)
                                    stopspeacking()
                            elif 'no' in confirmCreateRequest or 'non' in confirmCreateRequest or 'இல்லை' in confirmCreateRequest or 'नहीं' in confirmCreateRequest:
                                audio_string14 = 'This issue will not create without your confirmation.'
                                print(audio_string14)
                                destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                print(audio_string14)
                                talk(destini_lang14)
                                stopspeacking()
                            else:
                                audio_string11 = "Pardon!! Please confirm All these details are okay? Shall i proceed to create? please confirm yes or no"
                                print(audio_string11)
                                destini_lang11 = convert_language(audio_string11, choosenLangCode)
                                print(destini_lang11)
                                talk(destini_lang11)
                                confirmCreateRequest = multi_talk_command()
                                if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest or 'zee' in confirmCreateRequest or 'ss' in confirmCreateRequest or 'sí' in confirmCreateRequest or 'Oui' in confirmCreateRequest:
                                    print('BenchRequest Service..')
                                    benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                                    benchData = {"id": 0, "requestorId": 0, "requesterName": requesterName,
                                                 "stationId": 0, "stationName": stationName, "siteId": 1004,
                                                 "statusId": 3,
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
                                        audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                        print(audio_string12)
                                        destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                        talk(destini_lang12)
                                        print(destini_lang12)
                                        stopspeacking()
                                    else:
                                        audio_string13 = 'Thanks for using R1.0'
                                        print(audio_string13)
                                        destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                        talk(destini_lang13)
                                        print(destini_lang13)
                                        stopspeacking()
                                elif 'no' in confirmCreateRequest:
                                    audio_string14 = 'This issue will not create without your confirmation.'
                                    print(audio_string14)
                                    destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                    print(audio_string14)
                                    talk(destini_lang14)
                                    stopspeacking()
                                else:
                                    audio_string_out = "Sorry! Try to create ticket twice but the details not given proper continue if you want to do the same process"
                                    print(audio_string_out)
                                    destini_lang15 = convert_language(audio_string_out, choosenLangCode)
                                    print(destini_lang15)
                                    talk(destini_lang15)
        elif 'tamil' in choosenLangCode or 'hindi' in choosenLangCode:
            destini_lang0 = convert_language(audio_string, choosenLangCode)
            talk(destini_lang0)
            print(destini_lang0)
            requesterName = multi_talk_command_tamil(choosenLangCode)
            print(requesterName)
            command_reqname = convert_language(requesterName, "english")  # Using google to recognize audio
            print(command_reqname)
            if 'இல்லை' in requesterName or 'नहीं' in requesterName or 'nahin' in requesterName:
                audio_string1 = "Pardon! Can you tell your name again"
                print(audio_string1)
                destini_lang110 = convert_language(audio_string1, choosenLangCode)
                print(destini_lang110)
                talk(destini_lang110)
                requesterName = multi_talk_command_tamil(choosenLangCode)
                print(requesterName)
                command_reqname = convert_language(requesterName, "english")  # Using google to recognize audio
                print(command_reqname)
            else:
                audio_string2 = "Can you tell your stationName"
                print(audio_string2)
                destini_lang2 = convert_language(audio_string2, choosenLangCode)
                print(destini_lang2)
                talk(destini_lang2)
                stationName = multi_talk_command_tamil(choosenLangCode)
                print(stationName)
                command_stnname = convert_language(stationName, "english")  # Using google to recognize audio
                print(command_stnname)
                if 'இல்லை' in stationName or 'नहीं' in stationName or 'nahin' in stationName:
                    audio_string3 = "Pardon! Can you tell your stationName again"
                    print(audio_string3)
                    destini_lang3 = convert_language(audio_string3, choosenLangCode)
                    print(destini_lang3)
                    talk(destini_lang3)
                    stationName = multi_talk_command_tamil(choosenLangCode)
                    print(stationName)
                    command_stnname = convert_language(stationName, "english")  # Using google to recognize audio
                    print(command_stnname)
                else:
                    audio_string4 = "Can you describe issue"
                    print(audio_string4)
                    destini_lang4 = convert_language(audio_string4, choosenLangCode)
                    print(destini_lang4)
                    talk(destini_lang4)
                    reqIssueDescription = multi_talk_command_tamil(choosenLangCode)
                    print(reqIssueDescription)
                    command_descname = convert_language(reqIssueDescription, "english")
                    print(command_descname)
                    if 'இல்லை' in reqIssueDescription or 'नहीं' in reqIssueDescription or 'nahin' in reqIssueDescription:
                        audio_string5 = "Pardon! Can you describe the issue once again"
                        print(audio_string5)
                        destini_lang5 = convert_language(audio_string5, choosenLangCode)
                        print(destini_lang5)
                        talk(destini_lang5)
                        reqIssueDescription = multi_talk_command_tamil(choosenLangCode)
                        print(reqIssueDescription)
                        command_descname = convert_language(reqIssueDescription, "english")
                        print(command_descname)
                    else:
                        if 'இல்லை' in reqIssueDescription or 'இல்லை' in stationName or 'இல்லை' in requesterName or 'नहीं' in requesterName or 'nahin' in requesterName or 'नहीं' in stationName or 'nahin' in stationName or 'नहीं' in reqIssueDescription or 'nahin' in reqIssueDescription:
                            audio_string6 = "Pardon! The request not created due to invalid values.Please repeat"
                            print(audio_string6)
                            destini_lang6 = convert_language(audio_string6, choosenLangCode)
                            print(destini_lang6)
                            talk(destini_lang6)
                        else:
                            audio_string7 = "I am confirming the details as you given"
                            print(audio_string7)
                            destini_lang7 = convert_language(audio_string7, choosenLangCode)
                            talk(destini_lang7)
                            audio_string8 = "your name"
                            print(audio_string8)
                            destini_lang8 = convert_language(audio_string8, choosenLangCode)
                            print(destini_lang8)
                            talk(destini_lang8)
                            talk(command_reqname)
                            audio_string9 = "your station name"
                            print(audio_string9)
                            destini_lang9 = convert_language(audio_string9, choosenLangCode)
                            print(destini_lang9)
                            talk(destini_lang9)
                            talk(command_stnname)
                            print(stationName)
                            audio_string10 = "your issue description"
                            print(audio_string10)
                            destini_lang10 = convert_language(audio_string10, choosenLangCode)
                            print(destini_lang10)
                            talk(destini_lang10)
                            talk(command_descname)
                            print(reqIssueDescription)
                            audio_string11 = "All these details are okay? Shall i proceed to create? please confirm " \
                                             "yes or no "
                            print(audio_string11)
                            destini_lang11 = convert_language(audio_string11, choosenLangCode)
                            print(destini_lang11)
                            talk(destini_lang11)
                            confirmCreateRequest = multi_talk_command_tamil(choosenLangCode)
                            if 'yes' in confirmCreateRequest or 'हां' in confirmCreateRequest or 'theek hai' in confirmCreateRequest or 'ठीक है' in confirmCreateRequest or 'சரி' in confirmCreateRequest or 'ஆம்' in confirmCreateRequest or 'haan' in confirmCreateRequest:
                                print('BenchRequest Service..')
                                benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                                benchData = {"id": 0, "requestorId": 0, "requesterName": command_reqname,
                                             "stationId": 0, "stationName": command_stnname, "siteId": 1004,
                                             "statusId": 3,
                                             "categoryId": 1, "subcategoryId": 1, "assigneeId": 7668, "priority": 0,
                                             "repairAction1Id": 0, "repairAction2Id": 0, "repairAction3Id": 0,
                                             "diagnosisId": 0,
                                             "sBUId": 1, "systemId": 0, "description": command_descname,
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
                                    audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                    print(audio_string12)
                                    destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                    # talk(destini_lang12)
                                    print(destini_lang12)
                                    stopspeacking()
                                else:
                                    audio_string13 = 'Thanks for using R1.0'
                                    print(audio_string13)
                                    destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                    talk(destini_lang13)
                                    print(destini_lang13)
                                    stopspeacking()
                            elif 'no' in confirmCreateRequest or 'இல்லை' in confirmCreateRequest or 'नहीं' in confirmCreateRequest:
                                audio_string14 = 'This issue will not create without your confirmation.'
                                print(audio_string14)
                                destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                print(destini_lang14)
                                talk(destini_lang14)
                                stopspeacking()
        else:
            destini_lang0 = convert_language(audio_string, choosenLangCode)
            talk(destini_lang0)
            print(destini_lang0)
            requesterName = multi_talk_command()
            if 'None' in requesterName:
                audio_string1 = "Pardon! Can you tell your name again"
                print(audio_string1)
                destini_lang110 = convert_language(audio_string1, choosenLangCode)
                print(destini_lang110)
                talk(destini_lang110)
                requesterName = multi_talk_command()
                print(requesterName)
            else:
                audio_string2 = "Can you tell your stationName"
                print(audio_string2)
                destini_lang2 = convert_language(audio_string2, choosenLangCode)
                print(destini_lang2)
                talk(destini_lang2)
                stationName = multi_talk_command()
                print(stationName)
                if 'None' in stationName:
                    audio_string3 = "Pardon! Can you tell your stationName again"
                    print(audio_string3)
                    destini_lang3 = convert_language(audio_string3, choosenLangCode)
                    print(destini_lang3)
                    talk(destini_lang3)
                    stationName = multi_talk_command()
                    print(stationName)
                else:
                    audio_string4 = "Can you describe issue"
                    print(audio_string4)
                    destini_lang4 = convert_language(audio_string4, choosenLangCode)
                    print(destini_lang4)
                    talk(destini_lang4)
                    reqIssueDescription = multi_talk_command()
                    print(reqIssueDescription)
                    if 'None' in reqIssueDescription:
                        audio_string5 = "Pardon! Can you describe the issue once again"
                        print(audio_string5)
                        destini_lang5 = convert_language(audio_string5, choosenLangCode)
                        print(destini_lang5)
                        talk(destini_lang5)
                        reqIssueDescription = multi_talk_command()
                        print(reqIssueDescription)
                    else:
                        if 'None' in requesterName or 'None' in stationName or 'None' in reqIssueDescription:
                            audio_string6 = "Pardon! The request not created due to invalid values.Please repeat"
                            print(audio_string6)
                            destini_lang6 = convert_language(audio_string6, choosenLangCode)
                            print(destini_lang6)
                            talk(destini_lang6)
                        else:
                            audio_string7 = "I am confirming the details as you given"
                            print(audio_string7)
                            destini_lang7 = convert_language(audio_string7, choosenLangCode)
                            talk(destini_lang7)
                            audio_string8 = "your name"
                            print(audio_string8)
                            print(requesterName)
                            destini_lang8 = convert_language(audio_string8, choosenLangCode)
                            print(destini_lang8)
                            talk(destini_lang8)
                            talk(requesterName)
                            audio_string9 = "your station name"
                            print(audio_string9)
                            destini_lang9 = convert_language(audio_string9, choosenLangCode)
                            print(destini_lang9)
                            talk(destini_lang9)
                            talk(stationName)
                            audio_string10 = "your issue description"
                            print(audio_string10)
                            destini_lang10 = convert_language(audio_string10, choosenLangCode)
                            print(destini_lang10)
                            talk(destini_lang10)
                            talk(reqIssueDescription)
                            audio_string11 = "All these details are okay? Shall i proceed to create? please confirm yes or no"
                            print(audio_string11)
                            destini_lang11 = convert_language(audio_string11, choosenLangCode)
                            print(destini_lang11)
                            talk(destini_lang11)
                            confirmCreateRequest = multi_talk_command()
                            if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest or 'zee' in confirmCreateRequest or 'ss' in confirmCreateRequest or 'sí' in confirmCreateRequest or 'Oui' in confirmCreateRequest:
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
                                    audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                    print(audio_string12)
                                    destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                    talk(destini_lang12)
                                    print(destini_lang12)
                                    stopspeacking()
                                else:
                                    audio_string13 = 'Thanks for using R1.0'
                                    print(audio_string13)
                                    destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                    talk(destini_lang13)
                                    print(destini_lang13)
                                    stopspeacking()
                            elif 'no' in confirmCreateRequest or 'non' in confirmCreateRequest:
                                audio_string14 = 'This issue will not create without your confirmation.'
                                print(audio_string14)
                                destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                print(audio_string14)
                                talk(destini_lang14)
                                stopspeacking()
                            else:
                                audio_string11 = "Pardon!! Please confirm All these details are okay? Shall i proceed to create? please confirm yes or no"
                                print(audio_string11)
                                destini_lang11 = convert_language(audio_string11, choosenLangCode)
                                print(destini_lang11)
                                talk(destini_lang11)
                                confirmCreateRequest = multi_talk_command()
                                if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest or 'zee' in confirmCreateRequest or 'ss' in confirmCreateRequest or 'sí' in confirmCreateRequest or 'Oui' in confirmCreateRequest:
                                    print('BenchRequest Service..')
                                    benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                                    benchData = {"id": 0, "requestorId": 0, "requesterName": requesterName,
                                                 "stationId": 0, "stationName": stationName, "siteId": 1004,
                                                 "statusId": 3,
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
                                        audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                        print(audio_string12)
                                        destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                        talk(destini_lang12)
                                        print(destini_lang12)
                                        stopspeacking()
                                    else:
                                        audio_string13 = 'Thanks for using R1.0'
                                        print(audio_string13)
                                        destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                        talk(destini_lang13)
                                        print(destini_lang13)
                                        stopspeacking()
                                elif 'no' in confirmCreateRequest:
                                    audio_string14 = 'This issue will not create without your confirmation.'
                                    print(audio_string14)
                                    destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                    print(audio_string14)
                                    talk(destini_lang14)
                                    stopspeacking()
                                else:
                                    audio_string_out = "Sorry! Try to create ticket twice but the details not given proper continue if you want to do the same process"
                                    print(audio_string_out)
                                    destini_lang15 = convert_language(audio_string_out, choosenLangCode)
                                    print(destini_lang15)
                                    talk(destini_lang15)


    elif there_exists(["fedex", "tracking", "delivery", "where is package", "Shipment details"]):
        print("Am glad to help you on this, can you please provide me tracking number to get the status")
        talk("Am glad to help you on this, can you please provide me tracking number to get the status")
        print("sample tracking 123456789012/ 858488600850")
        print("122816215025810 = Delivered")
        print("020207021381215 = Picked Up")
        print("403934084723025 = Arrived at FedEx location")
        print("920241085725456 = At local FedEx facility")
        tracking_number = listen_trac_command()
        audio_tra7 = "I am confirming the details: the given tracking number is"
        print(audio_tra7)
        talk(audio_tra7)
        talk(tracking_number)
        print(tracking_number)
        tracking_number = re.sub(r'(\d)\s+(\d)', r'\1\2', tracking_number)
        print(tracking_number)
        tra_string11 = "All these details are okay? Shall i proceed to create? please confirm yes or no"
        print(tra_string11)
        talk(tra_string11)
        isconfirm = listen_trac_command()
        print(isconfirm)
        if 'yes' in isconfirm or 's' in isconfirm or 'z' in isconfirm or 'zee' in isconfirm or 'ss' in isconfirm or 'sí' in isconfirm or 'Oui' in isconfirm:
            print('Fedex track api loading ...')
            # fedex authorization
            authurl = "https://apis-sandbox.fedex.com/oauth/token"

            # payload = "grant_type=client_credentials&client_id=l7c83fd3c68c8049df93b5d72b8274641d&client_secret=2e09a50ac5fc428a9d24a891f919b1a5"

            payload = "grant_type=client_credentials&client_id=l7c302cd75cadf47b4aaced9a072fb8fb0&client_secret=e196e9e73338479d8e78ff44687e7d22"

            headers = {
                'Content-Type': "application/x-www-form-urlencoded"
            }
            authresponse = requests.request("POST", authurl, data=payload, headers=headers)

            # print(authresponse.text)
            print(json.loads(authresponse.text).get('access_token'))
            print(json.loads(authresponse.text)['access_token'])
            accessToken = json.loads(authresponse.text)['access_token']
            # print(accessToken)
            # time.sleep(5)

            url = "https://apis-sandbox.fedex.com/track/v1/associatedshipments"

            input1 = {
                  "includeDetailedScans": 1,
                  "associatedType": "STANDARD_MPS",
                  "masterTrackingNumberInfo": {
                    "shipDateEnd": "2022-03-15",
                    "shipDateBegin": "2022-03-01",
                    "trackingNumberInfo": {
                      "trackingNumberUniqueId": "245822~"+ tracking_number +"~FDEG",
                      "carrierCode": "FDXG",
                      "trackingNumber": tracking_number
                    }
                  },
                  "pagingDetails": {
                    "resultsPerPage": 56,
                    "pagingToken": "38903279038"
                  }
                }

            headers = {
                'Content-Type': "application/json",
                'X-locale': "en_US",
                'Authorization': "Bearer " + accessToken
            }
            print(headers)
            payload = json.dumps(input1)  # 'input' refers to JSON Payload
            print('after json_dumps')
            print(payload)
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            print('Fedex Service call in progress..')
            talk('Please Wait...Fedex Service call in progress..')
            # responeData = requests.request("POST", fedexReqUrl, data=fedexData, headers=headers)
            print("response.json()...................")
            responseData = response.text
            # print(responseData)
            # print(json.loads(responseData)['output'])
            # print(json.loads(responseData)['output']['completeTrackResults'])
            # outputres = json.loads(responseData)['output']['completeTrackResults'][0]['trackResults']
            # print(outputres)
            tracking_code = json.loads(responseData)['output']['completeTrackResults'][0]['trackResults'][0]['error']['code']
            tracking_msg =  json.loads(responseData)['output']['completeTrackResults'][0]['trackResults'][0]['error']['message']
            if response.status_code == 200:
                tra_string12 = 'Successfully located.And the message has been received from fedex is'
                print(tra_string12)
                talk(tra_string12)
                print(tracking_msg)
                talk(tracking_msg)
                tra_string112 = 'Thanks for using R1.0'
                print(tra_string112)
                talk(tra_string112)
            elif response.status_code == 400:
                tra_err = 'Sorry! not able to locate Please provide a valid reference/associated type'
                print(tra_err)
                talk(tra_err)
            elif response.status_code == 401:
                tra_err = 'Access token expired. Please modify your request and try again.'
                print(tra_err)
                talk(tra_err)
            elif response.status_code == 403:
                tra_err = 'We could not authorize your credentials. Please check your permissions and try again'
                print(tra_err)
                talk(tra_err)
            elif response.status_code == 404:
                tra_err = 'The resource you requested is no longer available. Please modify your request and try again'
                print(tra_err)
                talk(tra_err)
            elif response.status_code == 500:
                tra_err = 'We encountered an unexpected error and are working to resolve the issue. We apologize for any inconvenience. Please check back at a later time'
                print(tra_err)
                talk(tra_err)
            elif response.status_code == 503:
                tra_err = 'The service is currently unavailable and we are working to resolve the issue. We apologize for any inconvenience. Please check back at a later time.'
                print(tra_err)
                talk(tra_err)
            else:
                tra_string13 = 'Thanks for using R1.0'
                print(tra_string13)
                talk(tra_string13)
            stopspeacking()
        else:
            talk("Pardon! can you please come again the same")
            listen_trac_command()
            stopspeacking()

    elif there_exists(["play"]):
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)  # to play command from youtube
        print('playing')
        time.sleep(10)

    elif there_exists(["time"]):
        timenow = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + timenow)  # to get time
        print(timenow)
        time.sleep(1)

    elif there_exists(["wikipedia"]):
        talk('Searching Wikipedia...')
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)  # wikipedia about 1 line
        talk("According to Wikipedia")
        talk(info)
        print(info)
        time.sleep(1)

    elif there_exists(["open youtube"]):
        webbrowser.open_new_tab("https://www.youtube.com")
        talk("youtube is open now")
        time.sleep(5)

    elif there_exists(["open google", "google"]):
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")
        time.sleep(5)

    elif there_exists(["open contec", "company"]):
        webbrowser.open_new_tab("https://www.gocontec.com/")
        talk("Your company website is open now")
        time.sleep(5)

    elif there_exists(["open gmail", "gmail"]):
        webbrowser.open_new_tab("gmail.com")
        talk("Google Mail open now")
        time.sleep(5)

    elif there_exists(["open stackoverflow", "stackoverflow"]):
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        talk("Here is stackoverflow")
        time.sleep(5)

    elif there_exists(["open news", "news"]):
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif there_exists(["open new tab", "search"]):
        searchtxt = command.replace("search", "")
        webbrowser.open_new_tab(searchtxt)
        time.sleep(5)

    elif there_exists(["who are you", "what can you do"]):
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

    elif there_exists(["who made you", "who created you", "who discovered you"]):
        talk("I was made by Uma")
        print("I was made by Uma")

    elif there_exists(['how are you']):
        talk("I am fine, Thank you")
        talk("How are you")

    elif there_exists(['joke']):
        talk(pyjokes.get_joke())  # coding joke
        print(pyjokes.get_joke())
        time.sleep(1)

    elif there_exists(["log off", "sign out", "log out", "stop"]):
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


def there_exists(terms):
    for term in terms:
        if term in command:
            return True


def convert_language(audio_string, language_code):
    # invoking Translator
    if 'spanish' in language_code or 'french' in language_code:
        if 'spanish' in language_code:
            translate_text = translator.translate(audio_string, dest='es')
        elif 'french' in language_code:
            translate_text = translator.translate(audio_string, dest='fr')
        return translate_text.text
    elif 'tamil' in language_code or 'hindi' in language_code:
        print('am i here in tamil/hindi block?')
        if 'tamil' in language_code:
            print('am i here in tamil block?')
            translate_text = translator.translate(audio_string, dest='ta')
            print(translate_text)
            tts = gt.gTTS(text=translate_text.text, lang="ta", slow=False)
            basename = "tamilaudio"
            suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            filename = "_".join([basename, suffix])  # e.g. 'mylogfile_120508_171442'
            tts.save(filename + ".mp3")
            print(filename)
            os.system(filename + ".mp3")
            time.sleep(8)
        elif 'hindi' in language_code:
            translate_text = translator.translate(audio_string, dest='hi')
            tts = gt.gTTS(text=translate_text.text, lang="hi", slow=False)
            basename = "hindiaudio"
            suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            filename = "_".join([basename, suffix])  # e.g. 'mylogfile_120508_171442'
            tts.save(filename + ".mp3")
            os.system(filename + ".mp3")
            time.sleep(8)
        return translate_text.text
    else:
        translate_text = translator.translate(audio_string, dest='en')
        return translate_text.text


def startspeakeithme():
    wishMe()
    choosenLangcode = choose_language()
    choosenLangcode = choosenLangcode.lower()
    print(choosenLangcode)
    if "spanish" in choosenLangcode or "french" in choosenLangcode or "tamil" in choosenLangcode or "hindi" in choosenLangcode or "english" in choosenLangcode:
        print(choosenLangcode)
    else:
        print('please confirm your language')
        choosenLangcode = choose_language()
    # time.sleep()
    while True:
        run_alexa(choosenLangcode)


def stopspeacking():
    talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    sys.exit()


#   subprocess.call(["sleep", "/l"])

if __name__ == '__main__':
    global choosenLangCode

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
