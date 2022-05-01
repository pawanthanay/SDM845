
"""
File Name: PlayWAV
Description: Contains Playwav class with play_func with adb commands implementation
"""
import subprocess
from configparser import ConfigParser


class Playwav:

    """
    FunctionName: play_func
    Description: Plays WAV audio song using adb command
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
                "adb shell am start -a android.intent.action.VIEW -d file:///sdcard//Music//songs//sample.wav -t "
                "audio/wav")

            if config['Audio']['status'] == "playing":
                return "Playing"
            else:
                return "not playing"
        else:
            return "no Audio"
