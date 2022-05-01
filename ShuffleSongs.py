"""
File Name: ShuffleSong
Description: Contains Shuffle class with shuffle_func with adb commands implementation
"""

import os
import subprocess
from configparser import ConfigParser


class Shuffle:

    """
    FunctionName: shuffle_func
    Description: Plays audio song in shuffle all mode using adb commands
    Returns: String
    Input: None
    """
    @staticmethod
    def shuffle_func():
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

            for i in range(2):
                subprocess.call("adb shell input keyevent 66")

            # adb commands to close the music player application
            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH")
            subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
            subprocess.call("adb shell input keyevent DEL")
            if config['Audio']['modes'] == "shuffle":
                return "songs shuffled"
            else:
                return "failed"
        else:
            return "no audio"
