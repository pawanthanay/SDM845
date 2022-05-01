"""
File Name: AudioPause
Description: Contains Pause class with pause_func with adb commands implementation
"""

import subprocess
from time import sleep

from configparser import ConfigParser


class Pause:
    """
    FunctionName: Pause_func
    Description: Implements pause functionality using adb command
    Returns: String
    Input: None
    """
    @staticmethod
    def pause_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating the song name with the help of config file
        if config['Audio']['song'] == "playit":
            subprocess.call("adb shell am start -a android.intent.action.VIEW -d "
                            "file:///sdcard//Music//songs//sindhu.mp3 -t "
                            "audio/mp3")
            sleep(4)
            subprocess.call("adb shell input keyevent 85")
            sleep(1)
            subprocess.call("adb shell input keyevent 85")
            if config['Audio']['status'] != "playing":

                return "Paused"
            else:
                return "pause fail"
        else:
            return "no audio"
