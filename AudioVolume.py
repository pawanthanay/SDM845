"""
File Name: AudioVolume
Description: Contains Volume class with volume_func with adb commands implementation
"""

import subprocess
from time import sleep
from configparser import ConfigParser


class Volume:
    """
    FunctionName: volume_func
    Description: Implements volume change functionality using adb command
    Returns: String
    Input: None
    """

    @staticmethod
    def volume_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating the song name with the help of config file
        if config['Audio']['song'] == "playit":
            subprocess.call("adb shell input keyevent 85")
            subprocess.call("adb shell am start -a android.intent.action.VIEW -d "
                            "file:///sdcard//Music//songs//sindhu.mp3 -t "
                            "audio/mp3")
            subprocess.call("adb shell input keyevent 85")
            sleep(3)
            subprocess.call("adb shell input keyevent 24")
            subprocess.call("adb shell input keyevent 24")
            subprocess.call("adb shell input keyevent 24")
            sleep(2)
            subprocess.call("adb shell input keyevent 25")
            subprocess.call("adb shell input keyevent 25")
            subprocess.call("adb shell input keyevent 25")
            subprocess.call("adb shell input keyevent 25")
            sleep(2)
            subprocess.call("adb shell input keyevent 24")
            subprocess.call("adb shell input keyevent 24")
            if config['Audio']['volume'] == "50db":
                return "volume changed"
            else:
                return "not found"
        else:
            return "no audio"
