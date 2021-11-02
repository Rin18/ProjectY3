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

# READING AND WRITING WITH PICKLE
import pickle
fruits = ['apple','banana','pear']
#For writing:
with open('Fruits.obj', 'wb') as fp:
    pickle.dump(fruits, fp)

#For reading:
with open('Fruits.obj', 'rb') as fp:
    fruits = pickle.load(fp)

#Example for my case
notes_array = parse_midi("data/maestro_baroque/Purcell.mid")
with open('data/notes_parsed/notes', 'rb') as fp:
    parsed_notes = pickle.load(fp)
print("Notes read with function: \n", notes_array)

