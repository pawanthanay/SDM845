"""
File Name: DeleteSong
Description: Contains Delete class with delete_func with adb commands implementation
"""

import subprocess
from time import sleep
from configparser import ConfigParser


class Delete:

    """
    FunctionName: delete_func
    Description: Implements song delete functionality using adb command
    Returns: String
    Input: None
    """
    @staticmethod
    def delete_func():
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
            subprocess.call("adb shell input tap 1271 2271")
            subprocess.call("adb shell input tap 1013 1555")

            # adb commands to close the music player application
            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH")
            subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
            subprocess.call("adb shell input keyevent DEL")
            if config['Audio']['list'] == "empty":
                return "song deleted"
            else:
                return "not found"
        else:
            return "no audio"
