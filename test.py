#File for testing various things outside of maine
from functions import *
from music21 import *

dMaj = chord.Chord(['D', 'F#', 'A'])
myChord = chord.Chord('A4 C#5 E5')

notes = []
notes.append('.'.join(str(n) for n in dMaj.normalOrder))
notes.append('.'.join(str(n) for n in myChord.normalOrder))

print("Notes: ", notes)

output_midi(notes, "chord_test")
increased_chords = add_semitones(notes, 4)
output_midi(increased_chords, "increased_chords")

#with open('data/notes_parsed/notes', 'rb') as fp:
#    notes_array = pickle.load(fp)
#print("Notes from data folder: \n", notes_array)