import csv
# import parser
import webbrowser
from time import sleep
import configparser

import pandas as pd

from PlaySound import Play
from AudioPause import Pause
from AudioVolume import Volume
from RepeatAll import Repeat
from ShuffleSongs import Shuffle
from RepeatSong import RepeatOne
from DeleteSong import Delete
from SetRingtone import Ringtone
from TrickMode import Trick
from EqalizerEffect import Eqalizer
from PlayAMR import Playamr
from PlayFLAC import Playflac
from PlayM4A import Playm4a
from PlayOGG import Playogg
from PlayWAV import Playwav
from AudioQueue import AddQueue
from AudioShare import ShareAudio


first = Play()
pass_test1 = first.play_func()

sleep(4)
ffirst = Play()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test1 = ffirst.play_func()

sleep(3)
second = Pause()
pass_test2 = second.pause_func()

sleep(3)
fsecond = Pause()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'playing')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test2 = fsecond.pause_func()

sleep(3)
third = Volume()
pass_test3 = third.volume_func()

sleep(3)
fthird = Volume()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'volume', '10db')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test3 = fthird.volume_func()

sleep(7)
fourth = Repeat()
pass_test4 = fourth.repeat_func()

sleep(4)
ffourth = Repeat()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'mode', 'empty')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test4 = ffourth.repeat_func()

sleep(5)
fifth = Shuffle()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'modes', 'empty')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test5 = fifth.shuffle_func()

sleep(3)
ffifth = Shuffle()
fail_test5 = ffifth.shuffle_func()

sleep(3)
sixth = RepeatOne()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'mode', 'repeat')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test6 = sixth.repeatone_func()

sleep(3)
fsixth = RepeatOne()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'modes', 'empty')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test6 = fsixth.repeatone_func()

sleep(3)
seventh = Delete()
pass_test7 = seventh.delete_func()

sleep(3)
fseventh = Delete()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'list', 'full')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test7 = fseventh.delete_func()

sleep(3)
eight = Ringtone()
pass_test8 = eight.ringtone_func()

sleep(3)
feight = Ringtone()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'ringtone', 'newsong')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test8 = feight.ringtone_func()

sleep(3)
ninth = Trick()
pass_test9 = ninth.trick_func()

sleep(2)
fninth = Trick()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test9 = fninth.trick_func()

sleep(3)
tenth = Eqalizer()
pass_test10 = tenth.eqalizer_func()

sleep(4)
ftenth = Eqalizer()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'eqalizer', 'off')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test10 = ftenth.eqalizer_func()

sleep(3)
eleventh = Playamr()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'playing')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test11 = eleventh.play_func()

sleep(3)
feleventh = Playamr()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test11 = feleventh.play_func()

sleep(3)
twelfth = Playflac()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'playing')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test12 = twelfth.play_func()

sleep(3)
ftwelfth = Playflac()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test12 = ftwelfth.play_func()

sleep(3)
thirteen = Playm4a()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'playing')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test13 = thirteen.play_func()

sleep(3)
fthirteen = Playm4a()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test13 = fthirteen.play_func()

sleep(3)
fourteen = Playogg()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'playing')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test14 = fourteen.play_func()

sleep(3)
ffourteen = Playogg()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test14 = ffourteen.play_func()

sleep(3)
fifteen = Playwav()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'playing')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
pass_test15 = fifteen.play_func()

sleep(3)
ffifteen = Playwav()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'status', 'stop')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test15 = ffifteen.play_func()

sleep(3)
sixteen = ShareAudio()
pass_test16 = sixteen.shareaudio_func()

sleep(3)
fsixteen = ShareAudio()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'queue', 'empty')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test16 = fsixteen.shareaudio_func()

sleep(3)
seventeen = AddQueue()
pass_test17 = seventeen.addqueue_func()

sleep(3)
fseventeen = AddQueue()
config = configparser.ConfigParser()
config.read('config.ini')
config.set('Audio', 'queue', 'empty')
with open('config.ini', 'w') as configfile:
    config.write(configfile)
fail_test18 = fseventeen.addqueue_func()


with open('Output1.csv', 'w') as csvfile:
    fieldnames = ['MultimediaTC', 'Status', 'Reason', 'TestResult']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'MultimediaTC': 'AudioPause', 'Status': pass_test2,
                     'Reason': 'Music is paused', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': pass_test1,
                     'Reason': 'Music is played', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioVolume', 'Status': pass_test3,
                     'Reason': 'Volume is changed', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioRepeatAll', 'Status': pass_test4,
                     'Reason': 'Mode is changed to RepeatAll', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioShuffle', 'Status': pass_test5,
                     'Reason': 'Mode is changed to shuffleAll', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioRepeatOne', 'Status': pass_test6,
                     'Reason': 'Mode is changed to RepeatOne', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioDelete', 'Status': pass_test7,
                     'Reason': 'Music is Deleted', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioRingtone', 'Status': pass_test8,
                     'Reason': 'Music is set as ringtone', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioTrickMode', 'Status': pass_test9,
                     'Reason': 'Trick mode is working', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'EqalizerEffect', 'Status': pass_test10,
                     'Reason': 'equlizereffects', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': pass_test11,
                     'Reason': 'Music is played', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': pass_test12,
                     'Reason': 'Music is played', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': pass_test13,
                     'Reason': 'Music is played', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': pass_test14,
                     'Reason': 'Music is played', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': pass_test15,
                     'Reason': 'Music is played', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioShare', 'Status': pass_test16,
                     'Reason': 'Audio is shared', 'TestResult': "Pass"})
    writer.writerow({'MultimediaTC': 'AudioQueue', 'Status': pass_test17,
                     'Reason': 'Music is added to queue', 'TestResult': "Pass"})


a = pd.read_csv("Output1.csv")
a.to_html("TestC.html")
html_file = a.to_html()
webbrowser.open_new_tab('TestC.html')

with open('Output2.csv', 'w') as csvfile:
    fieldnames = ['MultimediaTC', 'Status', 'Reason', 'TestResult']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'MultimediaTC': 'AudioPause', 'Status': fail_test2,
                     'Reason': 'Music is not paused', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': fail_test1,
                     'Reason': 'Music is not played', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioVolume', 'Status': fail_test3,
                     'Reason': 'Volume is not changed', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioRepeatAll', 'Status': fail_test4,
                     'Reason': 'Mode is not changed to RepeatAll', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioShuffle', 'Status': fail_test5,
                     'Reason': 'Mode is not changed to shuffleAll', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioRepeatOne', 'Status': fail_test6,
                     'Reason': 'Mode is not changed to RepeatOne', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioDelete', 'Status': fail_test7,
                     'Reason': 'Music is not Deleted', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioRingtone', 'Status': fail_test8,
                     'Reason': 'Music is not set as ringtone', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioTrickMode', 'Status': fail_test9,
                     'Reason': 'Trick mode is not working', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'EqalizerEffect', 'Status': fail_test10,
                     'Reason': 'equlizereffects', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': fail_test11,
                     'Reason': 'Music is not played', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': fail_test12,
                     'Reason': 'Music is not played', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': fail_test13,
                     'Reason': 'Music is not played', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': fail_test14,
                     'Reason': 'Music is not played', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioPlay', 'Status': fail_test15,
                     'Reason': 'Music is not played', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioShare', 'Status': fail_test16,
                     'Reason': 'Music is not shared', 'TestResult': "Fail"})
    writer.writerow({'MultimediaTC': 'AudioQueue', 'Status': fail_test16,
                     'Reason': 'Not in Queue', 'TestResult': "Fail"})


a = pd.read_csv("Output2.csv")
a.to_html("TestC2.html")
html_file = a.to_html()
webbrowser.open_new_tab('TestC2.html')
