"""
File Name: EqalizerEffect
Description: Contains Eqalizer class with eqalizer_func with adb commands implementation
"""


import os
import subprocess
from time import sleep
from configparser import ConfigParser


class Eqalizer:

    """
    FunctionName: eqalizer_func
    Description: Implements different equalizer effects functionality using adb command
    Returns: String
    Input: None
    """
    @staticmethod
    def eqalizer_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating whether eqalizer effect is on or off
        if config['Audio']['eqalizer'] == "on":
            subprocess.call(
                "adb shell am start -a android.intent.action.VIEW -d file:///sdcard//Music//songs//sindhu.mp3 -t "
                "audio/mp3")
            sleep(3)
            os.system("adb shell input swipe 100 600 600 600 60")
            os.system("adb shell input touchscreen swipe 30 1800 600 1800")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 66")
            subprocess.call("adb shell input tap 937 447")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 66")
            sleep(5)
            subprocess.call("adb shell input tap 937 447")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 66")
            sleep(5)
            subprocess.call("adb shell input tap 937 447")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 66")
            sleep(5)
            subprocess.call("adb shell input tap 937 447")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 66")
            sleep(5)
            subprocess.call("adb shell input tap 937 447")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 20")
            subprocess.call("adb shell input keyevent 66")
            return "Pass"
        else:
            return "Fail"
