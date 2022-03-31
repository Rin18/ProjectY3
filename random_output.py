# This file contains the code to generate midi output of 500 random notes

from functions import *
import pickle
import random

# GENERATE_RANDOM
# Function that generates midi file compiled of random notes 
def generate_random():
    # load the notes used to train the model
    print("Loading the notes used to train the model")
    with open('data/notes_parsed/notes_bach', 'rb') as filepath:
        notes = pickle.load(filepath)

    # Get all pitch names
    pitchnames = sorted(set(item for item in notes))
    # Get all pitch names
    n_vocab = len(set(notes))
    # Get random notes sequence
    prediction_output = random_notes(pitchnames, n_vocab)
    # Convert sequence to midi
    output_midi(prediction_output, "random_bach")


# RANDOM_NOTES
# Function that, starting from a random point of sequence for prediction, 
# returns list of random notes
def random_notes(pitchnames, n_vocab):
    int_to_note = dict((number, note) for number, note in enumerate(pitchnames))
    prediction_output = []

    # generate 500 notes
    for note_index in range(500):
        index = random.randrange(0, n_vocab-1, 1)
        result = int_to_note[index]
        prediction_output.append(result)

    return prediction_output

generate_random()