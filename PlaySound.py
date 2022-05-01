"""
File Name: PlaySound
Description: Contains Play class with play_func with adb commands implementation
"""
import subprocess
from configparser import ConfigParser


class Play:
    """
    FunctionName: play_func
    Description: Plays audio song using adb command
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
                "adb shell am start -a android.intent.action.VIEW -d file:///sdcard//Music//songs//sindhu.mp3 -t "
                "audio/mp3")

            if config['Audio']['status'] == "playing":
                return "Playing"
            else:
                return "not playing"
        else:
            return "no Audio"
