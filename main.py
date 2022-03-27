# Initial main file to test things
from functions import *
from create_music import *

# Parse notes in dataset of midi files
path = 'data/test_dataset/'
notes = parse_midi(path)
#print("Result: \n", result)

# Incease notes by a tone and add them to array
increased_notes = add_semitones(notes, 2)
#print("Increased notes: \n", increased_notes)

#output_midi(increased_notes, "fur_elise")
output_midi(increased_notes, "test_new_parse_function")

generate()
