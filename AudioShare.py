"""
File Name: AudioShare
Description: Contains ShareAudio class with shareaudio_func with adb commands implementation
"""

import subprocess
from time import sleep
from configparser import ConfigParser


class ShareAudio:

    """
    FunctionName: shareaudio_func
    Description: Implements audio share functionality using adb command
    Returns: String
    Input: None
    """
    @staticmethod
    def shareaudio_func():
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
            subprocess.call("adb shell input tap 265 566")
            subprocess.call("adb shell input tap 1366 598")
            subprocess.call("adb shell input tap 909 2202")

            # adb commands to close the music player application
            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH")
            subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
            subprocess.call("adb shell input keyevent DEL")
            if config['Audio']['share'] == "pass":
                return "Audio share passed"
            else:
                return "Audio share failed"
        else:
            return "no audio"
