#File for testing various things outside of maine
from parse_midi import *
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