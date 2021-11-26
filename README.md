# VOICE AIDE


pyinstaller --onefile --icon="logo1.ico" --hidden-import pandas._libs.tslibs.base --hidden-import PIL._tkinter_finder --name="VOICEAIDE" -i "logo1.ico" aide.py
