"""
File Name: RepeatAll
Description: Contains Repeat class with repeat_func with adb commands implementation
"""

import os
import subprocess
from configparser import ConfigParser


class Repeat:

    """
    FunctionName: repeat_func
    Description: Plays audio song in repeat all mode using adb commands
    Returns: String
    Input: None
    """
    @staticmethod
    def repeat_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating the song name with the help of config file
        if config['Audio']['song'] == "playit":
            subprocess.call("adb shell am start -a android.intent.action.VIEW -d "
                            "file:///sdcard//Music//songs//sindhu.mp3 -t "
                            "audio/mp3")
            os.system("adb shell input swipe 100 600 600 600 60")
            os.system("adb shell input touchscreen swipe 30 1800 600 1800")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")

            for i in range(1):
                subprocess.call("adb shell input keyevent 66")

            # adb commands to close the music player application
            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH")
            subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
            subprocess.call("adb shell input keyevent DEL")
            if config['Audio']['mode'] == "repeat":
                return "RepeatAll mode"
            else:
                return "RepeatAll failed"
        else:
            return "no audio"
