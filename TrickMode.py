"""
File Name: TrickMode
Description: Contains Trick class with shuffle_func with adb commands implementation
"""
import subprocess
from time import sleep
from configparser import ConfigParser


class Trick:

    """
    FunctionName: trick_func
    Description: Plays audio song in repeat all mode using adb commands
    Returns: String
    Input: None
    """
    @staticmethod
    def trick_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating the song name with the help of config file
        if config['Audio']['song'] == "playit":
            sleep(3)
            subprocess.call(
                "adb shell am start -a android.intent.action.VIEW -d file:///sdcard//Music//songs//sindhu.mp3 -t "
                "audio/mp3")
            sleep(5)
            subprocess.call("adb shell input keyevent 87")
            sleep(5)
            subprocess.call("adb shell input keyevent 88")
            sleep(2)
            subprocess.call("adb shell input keyevent 87")
            sleep(2)
            subprocess.call("adb shell input keyevent 88")
            if config['Audio']['status'] == "playing":
                return "TrickMode check"
            else:
                return "failed"
        else:
            return "no audio"
