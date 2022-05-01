"""
File Name: SetRingtone
Description: Contains Ringtone class with ringtone_func with adb commands implementation
"""


import subprocess
from time import sleep
from configparser import ConfigParser


class Ringtone:

    """
    FunctionName: repeatone_func
    Description: Plays audio song in repeat all mode using adb commands
    Returns: String
    Input: None
    """

    @staticmethod
    def ringtone_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating the song name with the help of config file
        if config['Audio']['song'] == "playit":
            sleep(5)
            subprocess.call("adb shell am start -a android.intent.action.VIEW -d "
                            "file:///sdcard//Music//songs//sindhu.mp3 -t "
                            "audio/mp3")
            sleep(3)
            subprocess.call("adb shell input tap 534 2323")
            subprocess.call("adb shell input tap 1332 1831")
            subprocess.call("adb shell input tap 150 2185")

            # adb commands to close the music player application
            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH")
            subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
            subprocess.call("adb shell input keyevent DEL")
            if config['Audio']['ringtone'] == "playit":
                return "Ringtone set"
            else:
                return "Ringtone set failed"
        else:
            return "no audio"
