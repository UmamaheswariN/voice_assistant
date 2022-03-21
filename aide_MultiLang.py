import datetime
import os
import re
import sys  # to get exit
import time
import tkinter as tk
import webbrowser
import winsound
from logging import exception
from tkinter import *
import tkinter.messagebox as message
# from tkinter.ttk import *
import cv2
import gtts as gt
import json
import pyautogui
import pyjokes
import pyttsx3  # used to convert text to speech
import pywhatkit  # to play you tube music
import requests
import speech_recognition as sr  # used to convert human speech to text
import wikipedia
from GoogleNews import GoogleNews
from googletrans import Translator
from pygame import mixer

from weather import *

# import messagebox from tkinter module

global query

obj = tk.Tk()
obj.title("Contec Voice Assistant")
obj.geometry('800x500')
obj.resizable(False, False)
obj.config(bg='')

googlenews = GoogleNews()
translator = Translator()
listener = sr.Recognizer()  # initialization
engine = pyttsx3.init()  # used to talk
voices = engine.getProperty('voices')


def getCorrectPath(relative_path):
    p = os.path.abspath(".").replace('/dist', "")
    return os.path.join(p, relative_path)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def talk(command):
    engine = pyttsx3.init()  # used to talk
    #  voices = engine.getProperty('voices')
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)
    # Method for the speaking of the the assistant
    engine.say(command)
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.9)
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def detect_face():
    cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frames)
        speak("detecting face")
        print("Detecting face.....")
        time.sleep(10)
        pyautogui.press('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


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


def takeCommand():
    global query

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        # speak('Say that again please...')
        return "None"
    return query


def brightness():
    try:
        query = takeCommand().lower()
        if '25' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1610, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '50' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1684, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '75' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1758, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '100' in query or 'full' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1835, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        else:
            speak('Please select 25, 50, 75 or 100....... Say again.')
            brightness()
    except exception as e:
        # print(e)
        speak('Something went wrong')


def close_window():
    try:
        if 'y' in query:
            pyautogui.moveTo(1885, 10)
            pyautogui.click()
        else:
            speak('ok')
            pyautogui.moveTo(1000, 500)
    except exception as e:
        # print(e)
        speak('error')


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
        run_alexa(choosenLangCode)


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
                        "trackingNumberUniqueId": "245822~" + tracking_number + "~FDEG",
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
            tracking_code = json.loads(responseData)['output']['completeTrackResults'][0]['trackResults'][0]['error'][
                'code']
            tracking_msg = json.loads(responseData)['output']['completeTrackResults'][0]['trackResults'][0]['error'][
                'message']
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
            #stopspeacking()
        else:
            talk("Pardon! can you please come again the same")
            listen_trac_command()
            #stopspeacking()
        run_alexa(choosenLangCode)

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

    elif there_exists(['alarm']):
        alarm()

    elif there_exists(['hi', 'wake', 'hello', 'rithik', 'R1.0', 'R1', 'Hey', 'aur 1.0', 'uma']):
        speak('yes am here..Tell me how can i help you')

    elif there_exists(['change voice', 'change your voice']):
        engine.setProperty('voice', voices[1].id)
        speak("Here's an example of one of my voices. Would you like to use this one?")
        query1 = takeCommand().lower()
        if 'y' in query1 or 'sure' in query1 or 'of course' in query1:
            speak('Great. I will keep using this voice.')
            engine.setProperty('voice', voices[1].id)
        elif 'n' in query1:
            speak('Ok. I am back to my other voice.')
            engine.setProperty('voice', voices[0].id)
        else:
            speak('Sorry, I am having trouble understanding. I am back to my other voice.')
            engine.setProperty('voice', voices[0].id)

    elif there_exists(['increase', 'decrease', 'change', 'minimize', 'maximize']) and 'brightness' in command:
        speak('At what percent should I kept the brightness, 25, 50, 75 or 100?')
        brightness()

    elif there_exists(['piano']):
        speak('Yes, I can play piano.')
        winsound.Beep(200, 500)
        winsound.Beep(250, 500)
        winsound.Beep(300, 500)
        winsound.Beep(350, 500)
        winsound.Beep(400, 500)
        winsound.Beep(450, 500)
        winsound.Beep(500, 500)
        winsound.Beep(550, 500)

        time.sleep(6)

    elif (('open' in command or 'turn on' in command) and 'camera' in command) or (
            ('click' in command or 'take' in command) and ('photo' in command or 'pic' in command)):
        speak("Opening camera")
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0
        speak('say click, to click photo.....and if you want to turn off the camera, say turn off the camera')

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                speak('failed to grab frame')
                break
            cv2.imshow("test", frame)

            query3 = takeCommand().lower()
            k = cv2.waitKey(1)

            if 'click' in query3 or ('take' in query3 and 'photo' in query3):
                speak('Be ready!...... 3.....2........1..........')
                pyautogui.press('space')
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                speak('{} written!'.format(img_name))
                img_counter += 1
            elif 'escape' in query3 or 'off' in query3 or 'close' in query3:
                pyautogui.press('esc')
                print("Escape hit, closing...")
                speak('Turning off the camera')
                break
            elif k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:

                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                speak('{} written!'.format(img_name))
                img_counter += 1
            elif 'exit' in query3 or 'stop' in query3 or 'bye' in query3:
                speak('Please say, turn off the camera or press escape button before giving any other command')
            else:
                speak('I did not understand what did you say or you entered a wrong key.')

        cam.release()

        cv2.destroyAllWindows()

    elif there_exists(["log off", "sign out", "log out", "stop", "shut down", "exit", "bye"]):
        talk('Please give the review. It will help me to improve my performance.')
        select_review()

    elif 'screenshot' in command:
        speak('Please go on the screen whose screenshot you want to take, after 5 seconds I will take screenshot')
        time.sleep(4)
        speak('Taking screenshot....3........2.........1.......')
        pyautogui.screenshot('screenshot_by_r1.png')
        speak('The screenshot is saved as screenshot_by_r1.png')

    elif 'minimise' in command and 'screen' in command:
        pyautogui.moveTo(1770, 0)
        pyautogui.click()

    elif 'increase' in command and ('volume' in command or 'sound' in command):
        pyautogui.press('volumeup')

    elif 'decrease' in command and ('volume' in command or 'sound' in command):
        pyautogui.press('volumedown')

    elif 'capslock' in command or ('caps' in command and 'lock' in command):
        pyautogui.press('capslock')

    elif 'mute' in command:
        pyautogui.press('volumemute')

    elif 'currency' in command and 'conver' in command:
        speak(
            'I can convert, US dollar into indian rupee, and indian rupee into US dollar. Do you want to continue it?')
        query4 = takeCommand().lower()
        if 'y' in query4 or 'sure' in query4 or 'of course' in query4:
            speak('which conversion you want to do? US dollar to indian rupee, or indian rupee to US dollar?')
            query5 = takeCommand().lower()
            if ('dollar' in query5 or 'US' in query5) and ('to india' in query5 or 'to rupee' in query5):
                speak('Enter US Dollar')
                USD = float(input("Enter United States Dollar (USD):"))
                INR = USD * 74.8
                inr = "{:.4f}".format(INR)
                print(f"{USD} US Dollar is equal to {inr} indian rupee.")
                speak(f'{USD} US Dollar is equal to {inr} indian rupee.')
                speak("If you again want to do currency conversion then say, 'convert currency' ")
            elif ('india' in query5 or 'rupee' in query5) and (
                    'to US' in query5 or 'to dollar' in query5 or 'to US dollar'):
                speak('Enter Indian Rupee')
                INR = float(input("Enter Indian Rupee (INR):"))
                USD = INR / 74.8
                usd = "{:.3f}".format(USD)
                print(f"{INR} indian rupee is equal to {usd} US Dollar.")
                speak(f'{INR} indian rupee is equal to {usd} US Dollar.')
                speak("If you again want to do currency conversion then say, 'convert currency' ")
            else:
                speak(
                    "I cannot understand what did you say. If you want to convert currency just say 'convert currency'")
        else:
            print('ok Thank you')

    elif 'online shop' in command or (
            ('can' in command or 'want' in command or 'do' in command or 'could' in command) and 'shop' in command) or (
            'let' in command and 'shop' in command):
        speak('From which online shopping website, you want to shop? Amazon, flipkart, snapdeal or naaptol?')
        query6 = takeCommand().lower()
        if 'amazon' in query6:
            webbrowser.open('https://www.amazon.com')
            time.sleep(10)
        elif 'flip' in query6:
            webbrowser.open('https://www.flipkart.com')
            time.sleep(10)
        elif 'snap' in query6:
            webbrowser.open('https://www.snapdeal.com')
            time.sleep(10)
        elif 'na' in query6:
            webbrowser.open('https://www.naaptol.com')
            time.sleep(10)
        else:
            speak('Sorry , you have to search in browser as this shopping website is not reachable for me.')

    else:
        # talk('Please repeat again.')
        return 0


def select_review():
    global root3
    global vs
    global type_of_review
    root3 = Tk()
    root3.title("Select an option")

    vs = IntVar()
    string = "Are you satisfied with my performance?"
    msgbox = Message(root3, text=string)
    msgbox.config(bg="lightgreen", font="(20)")
    msgbox.grid(row=0, column=0)
    rs1 = Radiobutton(root3, text="Very Satisfied", font="(20)", value=1, variable=vs).grid(row=1, column=0, sticky=W)
    rs2 = Radiobutton(root3, text="Satisfied", font="(20)", value=2, variable=vs).grid(row=2, column=0, sticky=W)
    rs3 = Radiobutton(root3, text="Neither Satisfied Nor Dissatisfied", font="(20)", value=3, variable=vs).grid(row=3,
                                                                                                                column=0,
                                                                                                                sticky=W)
    rs4 = Radiobutton(root3, text="Dissatisfied", font="(20)", value=4, variable=vs).grid(row=4, column=0, sticky=W)
    rs5 = Radiobutton(root3, text="Very Dissatisfied", font="(20)", value=5, variable=vs).grid(row=5, column=0,
                                                                                               sticky=W)
    rs6 = Radiobutton(root3, text="I don't want to give review", font="(20)", value=6, variable=vs).grid(row=6,
                                                                                                         column=0,
                                                                                                         sticky=W)

    bs = Button(root3, text="Submit", font="(20)", activebackground="yellow", activeforeground="green", command=select1)
    bs.grid(row=7, columnspan=2)

    root3.mainloop()

def select1():
    global vs
    global root3
    global type_of_review

    if vs.get() == 1:
        message.showinfo(" ","Thank you for your review!!")
        review = "Very Satisfied"
        type_of_review = "Positive"
        root3.destroy()
    elif vs.get() == 2:
        message.showinfo(" ","Thank you for your review!!")
        review = "Satisfied"
        type_of_review = "Positive"
        root3.destroy()
    elif vs.get() == 3:
        message.showinfo(" ","Thank you for your review!!!!")
        review = "Neither Satisfied Nor Dissatisfied"
        type_of_review = "Neutral"
        root3.destroy()
    elif vs.get() == 4:
        message.showinfo(" ","Thank you for your review!!")
        review = "Dissatisfied"
        type_of_review = "Negative"
        root3.destroy()
    elif vs.get() == 5:
        message.showinfo(" ","Thank you for your review!!")
        review = "Very Dissatisfied"
        type_of_review = "Negative"
        root3.destroy()
    elif vs.get() == 6:
        message.showinfo(" ","    Ok    ")
        review = "I do not want to give review"
        type_of_review = "No review"
        root3.destroy()
    try:
        print('Thanks for your review')
        talk("Thanks for your review")
        talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        sys.exit()
    except Exception as e:
        pass

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
    # detect_face()
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


def alarm():
    root = Tk()
    hrs = StringVar()
    mins = StringVar()
    secs = StringVar()
    root.title('R1.0 Alarm-Clock')
    speak('Please enter the time in the format hour, minutes and seconds. When the alarm should rang?')
    speak('Please enter the time greater than the current time')

    def setalarm():
        alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
        print(alarmtime)
        if alarmtime != "::":
            alarmclock(alarmtime)
        else:
            speak('You have not entered the time.')

    def alarmclock(alarmtime):
        print("am in alaramclock fun")
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        while True:
            time.sleep(1)
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            if time_now == alarmtime:
                Wakeup = Label(root, font=('arial', 20, 'bold'), text="Wake up! Wake up! Wake up", bg="DodgerBlue2",
                               fg="white").grid(row=6, columnspan=3)
                talk("Wake up, Have a good day")
                print("Wake up!")
                mixer.init()
                mixer.music.load(r'Music/Runaway-Aurora.mp3')
                mixer.music.play()
                break
        talk('you can click on close icon to close the alarm window.')

    greet = Label(root, font=('arial', 20, 'bold'), text="Take a short nap!").grid(row=1, columnspan=3)
    hrbtn = Entry(root, textvariable=hrs, width=5, font=('arial', 20, 'bold'))
    hrbtn.grid(row=2, column=1)
    minbtn = Entry(root, textvariable=mins, width=5, font=('arial', 20, 'bold')).grid(row=2, column=2)
    secbtn = Entry(root, textvariable=secs, width=5, font=('arial', 20, 'bold')).grid(row=2, column=3)
    setbtn = Button(root, text="set alarm", command=setalarm, bg="DodgerBlue2", fg="white",
                    font=('arial', 20, 'bold')).grid(row=4, columnspan=3)
    timeleft = Label(root, font=('arial', 20, 'bold'))
    timeleft.grid()
    mainloop()


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
