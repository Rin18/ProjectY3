""""
files=["MIDI-UNPROCESSED_01-03_R1_2014_MID--AUDIO_01_R1_2014_wav--2.midiORORORMIDI-Unprocessed_14_R1_2009_01-05_ORIG_MID--AUDIO_14_R1_2009_14_R1_2009_04_WAV.midiORORORMIDI-Unprocessed_01_R1_2009_01-04_ORIG_MID--AUDIO_01_R1_2009_01_R1_2009_01_WAV.midiORORORMIDI-Unprocessed_Recital5-7_MID--AUDIO_07_R1_2018_wav--3.midiORORORMIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_13_R1_2014_wav--1.midiORORORMIDI-Unprocessed_09_R1_2009_01-04_ORIG_MID--AUDIO_09_R1_2009_09_R1_2009_02_WAV.midiOR"\
"ORORMIDI-UNPROCESSED_19-21_R3_2014_MID--AUDIO_21_R3_2014_wav--1.midiORORORMIDI-Unprocessed_14_R1_2009_01-05_ORIG_MID--AUDIO_14_R1_2009_14_R1_2009_03_WAV.midiOR"\
"ORORMIDI-UNPROCESSED_09-10_R1_2014_MID--AUDIO_10_R1_2014_wav--2.midiORORORMIDI-UNPROCESSED_09-10_R1_2014_MID--AUDIO_10_R1_2014_wav--1.midiOR"\
"ORORMIDI-UNPROCESSED_01-03_R1_2014_MID--AUDIO_01_R1_2014_wav--1.midiORORORMIDI-Unprocessed_01_R1_2009_01-04_ORIG_MID--AUDIO_01_R1_2009_01_R1_2009_02_WAV.midiOR"\
"ORORMIDI-UNPROCESSED_19-21_R3_2014_MID--AUDIO_21_R3_2014_wav--2.midiOR"\
"ORORMIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_13_R1_2014_wav--2.midiOR"\
"ORORMIDI-Unprocessed_02_R1_2009_01-02_ORIG_MID--AUDIO_02_R1_2009_02_R1_2009_01_WAV.midiOR"\
"ORORMIDI-Unprocessed_10_R2_2008_01-05_ORIG_MID--AUDIO_10_R2_2008_wav--2.midiOR"\
"ORORMIDI-Unprocessed_Recital17-19_MID--AUDIO_18_R1_2018_wav--3.midiORORORMIDI-UNPROCESSED_04-05_R1_2014_MID--AUDIO_04_R1_2014_wav--1.midiORORORMIDI-Unprocessed_Recital9-11_MID--AUDIO_09_R1_2018_wav--6.midiORORMIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_11_R1_2014_wav--2.midiORORORMIDI-Unprocessed_Recital9-11_MID--AUDIO_09_R1_2018_wav--5.midiOR"\
"ORORMIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_11_R1_2014_wav--1.midiOR"\
"ORORMIDI-Unprocessed_10_R2_2008_01-05_ORIG_MID--AUDIO_10_R2_2008_wav--1.midiOR"\
"ORORMIDI-Unprocessed_083_PIANO083_MID--AUDIO-split_07-09-17_Piano-e_2_-06_wav--1.midiOR"\
"ORORMIDI-Unprocessed_14_R1_2009_01-05_ORIG_MID--AUDIO_14_R1_2009_14_R1_2009_05_WAV.midiORORORMIDI-Unprocessed_083_PIANO083_MID--AUDIO-split_07-09-17_Piano-e_2_-06_wav--2.midiORORORMIDI-Unprocessed_XP_04_R1_2004_03-05_ORIG_MID--AUDIO_04_R1_2004_06_Track06_wav.midi"]
"""
import os
import shutil

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


files = "MIDI-Unprocessed_09_R3_2008_01-07_ORIG_MID--AUDIO_09_R3_2008_wav--3.midi OR "\
"MIDI-Unprocessed_09_R3_2008_01-07_ORIG_MID--AUDIO_09_R3_2008_wav--2.midi OR "\
"MIDI-Unprocessed_09_R3_2008_01-07_ORIG_MID--AUDIO_09_R3_2008_wav--1.midi OR "\
"MIDI-UNPROCESSED_01-03_R1_2014_MID--AUDIO_01_R1_2014_wav--2.midi OR "\
"MIDI-Unprocessed_14_R1_2009_01-05_ORIG_MID--AUDIO_14_R1_2009_14_R1_2009_04_WAV.midi OR "\
"MIDI-Unprocessed_01_R1_2009_01-04_ORIG_MID--AUDIO_01_R1_2009_01_R1_2009_01_WAV.midi OR "\
"MIDI-Unprocessed_Recital5-7_MID--AUDIO_07_R1_2018_wav--3.midi OR "\
"MIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_13_R1_2014_wav--1.midi OR "\
"MIDI-Unprocessed_09_R1_2009_01-04_ORIG_MID--AUDIO_09_R1_2009_09_R1_2009_02_WAV.midi OR "\
"MIDI-UNPROCESSED_19-21_R3_2014_MID--AUDIO_21_R3_2014_wav--1.midi OR "\
"MIDI-Unprocessed_14_R1_2009_01-05_ORIG_MID--AUDIO_14_R1_2009_14_R1_2009_03_WAV.midi OR MIDI-UNPROCESSED_09-10_R1_2014_MID--AUDIO_10_R1_2014_wav--2.midi OR MIDI-UNPROCESSED_09-10_R1_2014_MID--AUDIO_10_R1_2014_wav--1.midi OR MIDI-UNPROCESSED_01-03_R1_2014_MID--AUDIO_01_R1_2014_wav--1.midi OR MIDI-Unprocessed_01_R1_2009_01-04_ORIG_MID--AUDIO_01_R1_2009_01_R1_2009_02_WAV.midi OR MIDI-UNPROCESSED_19-21_R3_2014_MID--AUDIO_21_R3_2014_wav--2.midi OR MIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_13_R1_2014_wav--2.midi OR MIDI-Unprocessed_02_R1_2009_01-02_ORIG_MID--AUDIO_02_R1_2009_02_R1_2009_01_WAV.midi OR MIDI-Unprocessed_10_R2_2008_01-05_ORIG_MID--AUDIO_10_R2_2008_wav--2.midi OR MIDI-Unprocessed_Recital17-19_MID--AUDIO_18_R1_2018_wav--3.midi OR MIDI-UNPROCESSED_04-05_R1_2014_MID--AUDIO_04_R1_2014_wav--1.midi OR MIDI-Unprocessed_Recital9-11_MID--AUDIO_09_R1_2018_wav--6.midi OR MIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_11_R1_2014_wav--2.midi OR MIDI-Unprocessed_Recital9-11_MID--AUDIO_09_R1_2018_wav--5.midi OR MIDI-UNPROCESSED_11-13_R1_2014_MID--AUDIO_11_R1_2014_wav--1.midi OR MIDI-Unprocessed_10_R2_2008_01-05_ORIG_MID--AUDIO_10_R2_2008_wav--1.midi OR MIDI-Unprocessed_083_PIANO083_MID--AUDIO-split_07-09-17_Piano-e_2_-06_wav--1.midi OR MIDI-Unprocessed_14_R1_2009_01-05_ORIG_MID--AUDIO_14_R1_2009_14_R1_2009_05_WAV.midi OR MIDI-Unprocessed_083_PIANO083_MID--AUDIO-split_07-09-17_Piano-e_2_-06_wav--2.midi OR MIDI-Unprocessed_XP_04_R1_2004_03-05_ORIG_MID--AUDIO_04_R1_2004_06_Track06_wav.midi"


files_Bach = ",MIDI-Unprocessed_Recital17-19_MID--AUDIO_19_R1_2018_wav--1.midi "\
",MIDI-UNPROCESSED_04-05_R1_2014_MID--AUDIO_05_R1_2014_wav--1.midi"\
",MIDI-Unprocessed_R2_D2-19-21-22_mid--AUDIO-from_mp3_19_R2_2015_wav--1.midi"\
",MIDI-Unprocessed_06_R1_2009_03-07_ORIG_MID--AUDIO_06_R1_2009_06_R1_2009_03_WAV.midi"\
",MIDI-Unprocessed_06_R1_2009_03-07_ORIG_MID--AUDIO_06_R1_2009_06_R1_2009_04_WAV.midi"\
",MIDI-Unprocessed_R1_D1-1-8_mid--AUDIO-from_mp3_08_R1_2015_wav--1.midi"\
",MIDI-Unprocessed_Recital5-7_MID--AUDIO_06_R1_2018_wav--1.midi"\
",ORIG-MIDI_01_7_10_13_Group_MID--AUDIO_08_R3_2013_wav--2.midi"\
",MIDI-Unprocessed_08_R1_2008_01-05_ORIG_MID--AUDIO_08_R1_2008_wav--1.midi"\
",MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.midi"\
",MIDI-Unprocessed_SMF_22_R1_2004_01-04_ORIG_MID--AUDIO_22_R1_2004_03_Track03_wav.midi"\
",MIDI-Unprocessed_SMF_22_R1_2004_01-04_ORIG_MID--AUDIO_22_R1_2004_05_Track05_wav.midi"\
",MIDI-UNPROCESSED_16-18_R1_2014_MID--AUDIO_18_R1_2014_wav--1.midi"\
",MIDI-Unprocessed_Recital13-15_MID--AUDIO_14_R1_2018_wav--1.midi"\
",MIDI-Unprocessed_R2_D1-2-3-6-7-8-11_mid--AUDIO-from_mp3_07_R2_2015_wav--1.midi"\
",ORIG-MIDI_01_7_10_13_Group_MID--AUDIO_07_R3_2013_wav--1.midi"\
",MIDI-UNPROCESSED_14-15_R1_2014_MID--AUDIO_14_R1_2014_wav--1.midi"\
",ORIG-MIDI_02_7_8_13_Group__MID--AUDIO_12_R2_2013_wav--1.midi"\
",MIDI-Unprocessed_Chamber4_MID--AUDIO_11_R3_2018_wav--1.midi"\
",MIDI-Unprocessed_10_R1_2009_01-02_ORIG_MID--AUDIO_10_R1_2009_10_R1_2009_01_WAV.midi"\
",MIDI-UNPROCESSED_06-08_R1_2014_MID--AUDIO_07_R1_2014_wav--2.midi"\
",MIDI-Unprocessed_17_R1_2006_01-06_ORIG_MID--AUDIO_17_R1_2006_01_Track01_wav.midi"\
",MIDI-Unprocessed_19_R1_2006_01-07_ORIG_MID--AUDIO_19_R1_2006_01_Track01_wav.midi"\
",ORIG-MIDI_01_7_6_13_Group__MID--AUDIO_02_R1_2013_wav--1.midi"\
",MIDI-Unprocessed_SMF_17_R1_2004_01-02_ORIG_MID--AUDIO_20_R2_2004_02_Track02_wav.midi"\
",MIDI-Unprocessed_11_R1_2011_MID--AUDIO_R1-D4_07_Track07_wav.midi"\
",MIDI-Unprocessed_R1_D1-1-8_mid--AUDIO-from_mp3_02_R1_2015_wav--1.midi"\
",MIDI-Unprocessed_R1_D2-13-20_mid--AUDIO-from_mp3_16_R1_2015_wav--1.midi"\
",MIDI-Unprocessed_R1_D2-13-20_mid--AUDIO-from_mp3_13_R1_2015_wav--1.midi"\
",MIDI-Unprocessed_19_R1_2011_MID--AUDIO_R1-D7_12_Track12_wav.midi"\
",MIDI-Unprocessed_25_R1_2011_MID--AUDIO_R1-D9_14_Track14_wav.midi"\
",MIDI-Unprocessed_067_PIANO067_MID--AUDIO-split_07-07-17_Piano-e_3-03_wav--1.midi"\
",MIDI-Unprocessed_06_R1_2011_MID--AUDIO_R1-D2_14_Track14_wav.midi"\
",ORIG-MIDI_03_7_6_13_Group__MID--AUDIO_09_R1_2013_wav--1.midi"\
",MIDI-Unprocessed_R1_D1-9-12_mid--AUDIO-from_mp3_12_R1_2015_wav--1.midi"\
",MIDI-Unprocessed_15_R1_2011_MID--AUDIO_R1-D6_07_Track07_wav.midi"\
",MIDI-Unprocessed_052_PIANO052_MID--AUDIO-split_07-06-17_Piano-e_3-03_wav--2.midi"\
",MIDI-Unprocessed_054_PIANO054_MID--AUDIO-split_07-07-17_Piano-e_1-02_wav--1.midi"\
",MIDI-Unprocessed_062_PIANO062_MID--AUDIO-split_07-07-17_Piano-e_2-07_wav--2.midi"\
",MIDI-Unprocessed_13_R1_2008_01-04_ORIG_MID--AUDIO_13_R1_2008_wav--1.midi"\
",ORIG-MIDI_01_7_6_13_Group__MID--AUDIO_04_R1_2013_wav--1.midi"\
",MIDI-UNPROCESSED_01-03_R1_2014_MID--AUDIO_03_R1_2014_wav--2.midi"\
",MIDI-Unprocessed_09_R1_2011_MID--AUDIO_R1-D3_12_Track12_wav.midi"\
",MIDI-Unprocessed_055_PIANO055_MID--AUDIO-split_07-07-17_Piano-e_1-04_wav--1.midi"\
",MIDI-Unprocessed_06_R1_2008_01-04_ORIG_MID--AUDIO_06_R1_2008_wav--1.midi"\
",MIDI-Unprocessed_09_R1_2008_01-05_ORIG_MID--AUDIO_09_R1_2008_wav--1.midi"\
",ORIG-MIDI_03_7_6_13_Group__MID--AUDIO_10_R1_2013_wav--1.midi"\
",MIDI-Unprocessed_XP_03_R1_2004_01-02_ORIG_MID--AUDIO_03_R1_2004_01_Track01_wav.midi"\
",MIDI-Unprocessed_R1_D2-21-22_mid--AUDIO-from_mp3_22_R1_2015_wav--1.midi"\
",ORIG-MIDI_02_7_7_13_Group__MID--AUDIO_15_R1_2013_wav--1.midi"\
",ORIG-MIDI_02_7_7_13_Group__MID--AUDIO_18_R1_2013_wav--1.midi"\
",MIDI-Unprocessed_16_R1_2011_MID--AUDIO_R1-D6_12_Track12_wav.midi"\
",MIDI-Unprocessed_03_R1_2008_01-04_ORIG_MID--AUDIO_03_R1_2008_wav--1.midi"\
",MIDI-Unprocessed_R1_D2-13-20_mid--AUDIO-from_mp3_17_R1_2015_wav--1.midi"\
",MIDI-UNPROCESSED_16-18_R1_2014_MID--AUDIO_16_R1_2014_wav--1.midi"\
",MIDI-Unprocessed_R1_D2-13-20_mid--AUDIO-from_mp3_20_R1_2015_wav--1.midi"\
",MIDI-Unprocessed_21_R1_2011_MID--AUDIO_R1-D8_07_Track07_wav.midi"\
",MIDI-Unprocessed_24_R1_2011_MID--AUDIO_R1-D9_08_Track08_wav.midi"\
",MIDI-Unprocessed_04_R1_2011_MID--AUDIO_R1-D2_02_Track02_wav.midi"\
",MIDI-Unprocessed_12_R1_2011_MID--AUDIO_R1-D4_15_Track15_wav.midi"\
",MIDI-UNPROCESSED_01-03_R1_2014_MID--AUDIO_02_R1_2014_wav--1.midi"\
",ORIG-MIDI_01_7_7_13_Group__MID--AUDIO_13_R1_2013_wav--1.midi"\
",MIDI-Unprocessed_02_R1_2008_01-05_ORIG_MID--AUDIO_02_R1_2008_wav--1.midi"\
",MIDI-Unprocessed_10_R1_2008_01-04_ORIG_MID--AUDIO_10_R1_2008_wav--1.midi"

files_Hendel = "MIDI-Unprocessed_18_R1_2009_01-03_ORIG_MID--AUDIO_18_R1_2009_18_R1_2009_01_WAV.midi,MIDI-Unprocessed_Recital1-3_MID--AUDIO_01_R1_2018_wav--1.midi,MIDI-Unprocessed_079_PIANO079_MID--AUDIO-split_07-09-17_Piano-e_1-04_wav--1.midi,MIDI-Unprocessed_XP_08_R1_2004_01-02_ORIG_MID--AUDIO_08_R1_2004_01_Track01_wav.midi,MIDI-Unprocessed_12_R1_2009_01-02_ORIG_MID--AUDIO_12_R1_2009_12_R1_2009_01_WAV.midi"

names = files_Hendel.split(",")
#print(files_Hendel)
#print(names)
#print(len(names))

path_curr = os.getcwd()
data_path = "/mnt/d/Coding/MyProject/RomanticPeriodML/ProjectY3/data/maestro_baroque"
path_array = []
for name in names:
    result = find(name, path_curr)
    path_array.append(result) 
print(path_array)

for paths in path_array:
    if paths != None:
        print(paths)
        shutil.copy(paths, data_path)


