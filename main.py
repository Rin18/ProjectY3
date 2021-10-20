#Initial main file to test things

from parse_midi import *

#Parse notes in one midi file
#notes = parse_midi("data/for_elise_by_beethoven.mid")
notes = parse_midi("data/maestro_baroque/Purcell.mid")
#print("Result: \n", result)

# Incease notes by a tone and add them to array
increased_notes = add_semitones(notes, 2)
#print("Increased notes: \n", increased_notes)

#output_midi(increased_notes, "fur_elise")
output_midi(increased_notes, "Purcell")