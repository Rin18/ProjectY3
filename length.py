# Python script to calculate total number of seconds of dataset

import os
from mido import MidiFile

files = os.listdir()
print(files)

total_seconds = 0
for song in files:
    if song != 'length.py':
        mid = MidiFile(song)
    print("Working on: ", song)
    total_seconds = total_seconds + mid.length
print("Total seconds = ", total_seconds)