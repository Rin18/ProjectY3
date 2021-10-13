#Just In Case
#File for discarded ideas that might be needed later
import random
from parse_midi import *

result = parse_midi("for_elise_by_beethoven.mid")
#Trying to work out note to int and int to note
unique_notes = list(set(result))
n_notes = len(unique_notes)
#print("Notes nr: \n", n_notes)



# MAP INTEGER -> NOTE AND NOTE -> INTEGER
note_to_int = dict((note, number) for number, note in enumerate(unique_notes))
print("note_to_int: \n", note_to_int)

#int_to_note = dict((number, note_) for number, note_ in enumerate(unique_notes)) 
#predicted_notes = [int_to_note[i] for i in predictions]

#Generate random notes
def generate_notes(pitchnames, n_vocab):
    int_to_note = dict((number, note) for number, note in enumerate(pitchnames))
    predicted_notes = []

    for note_index in range(100):
        index = random.randrange(0, n_vocab-1, 1)
        result = int_to_note[index]
        predicted_notes.append(result)

    return predicted_notes

predicted_notes = generate_notes(unique_notes, n_notes)
print("Predicted notes: \n", predicted_notes)
