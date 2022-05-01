
"""
File Name: PlayM4A
Description: Contains Playm4a class with play_func with adb commands implementation
"""
import subprocess
from configparser import ConfigParser


class Playm4a:

    """
    FunctionName: play_func
    Description: Plays M4A audio song using adb command
    Returns: String
    Input: None
    """
    @staticmethod
    def play_func():
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        # Validating the song name with the help of config file
        if config['Audio']['song'] == "playit":
            subprocess.call(
                "adb shell am start -a android.intent.action.VIEW -d file:///sdcard//Music//songs//sample.m4a -t "
                "audio/m4a")

            if config['Audio']['status'] == "playing":
                return "Playing"
            else:
                return "not playing"
        else:
            return "no Audio"
