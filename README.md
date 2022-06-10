# VOICE AIDE


pyinstaller --onefile --icon="logo1.ico" --hidden-import pandas._libs.tslibs.base --hidden-import PIL._tkinter_finder --name="VOICEAIDE" -i "logo1.ico" aide.py

**Libraries setup:-**
1. Pycharm editor
2. python speech Recognition - pip install SpeechRecognition
3. pyttsx3 2.90 - pip install pyttsx3
4.python audio - pip install PyAudio - if we get error any time , we need to install pipwin by using below cmd,

pip install SpeechRecognition
pip install pyttsx3
pip install pipwin
then pipwin install Pyaudio

pip install pywhatkit - for utube
pip install wikipedia
pip install pyjokes
pip install python-utils


**Features in voice assistant:**

**version 1**:
1. Bench request
2. open browser
3. wikipedia
4. maps
5. weather
6. time
7. Spanish/french translation
8. tamil/hindi - translation (not 100%)
9. to play you tube music
10. open stackoverflow and any websites 

**version 2:**
1. Fedex:
	Tracking api integration done
	Ship api integration done
	rates api integration done
2. set alarm 
3. take screenshot
4. online shopping sites open
5. currency conversion (Indian to dollar vice versa)
7. system ctrls:
	Mute
	brightness
	Capslock
	increase volume/down
	minimize/maximize/close window
8. playing piano basic
