# This file generates music using a trained model

from functions import *
from keras.layers import BatchNormalization as BatchNorm
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation
from keras.models import Sequential
import numpy

# GENERATE
# Function that generates music
def generate():
    # Get the notes used in training the model
    with open('data/notes_parsed/notes_classical_test', 'rb') as filepath:
        notes = pickle.load(filepath)
    
    #with open('data/notes_parsed/notes_class', 'rb') as filepath:
    #    notes = pickle.load(filepath)

    # Pitch names from notes set
    pitchnames = sorted(set(item for item in notes))
    # Length of notes set
    notes_len = len(set(notes))
    # Create network input
    network_input, normalized_input = get_input(notes, pitchnames, notes_len)
    # Create model
    model = create_network(normalized_input, notes_len)
    # Prediction output used for generating notes
    prediction_output = predicted_notes(model, network_input, pitchnames, notes_len)
    # Convert prediction output to a midi file
    output_midi(prediction_output, "test_classical")

# GET_INPUT
# Function that given parsed notes as argument, shapes them as input for model
def get_input(notes, pitchnames, notes_len):
    # Note to integer map
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
    sequence_length = 100
    # sequence_length = 250
    network_input = []
    
    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])
    
    # Innput is incompatible with LSTM layers, fix that
    n_patterns = len(network_input)
    normalized_input = numpy.reshape(network_input, (n_patterns, sequence_length, 1))
    normalized_input = normalized_input / float(notes_len)
    return (network_input, normalized_input)

# CREATE_NETWORK
# Function for creating the LSTM neural network
def create_network(network_input, notes_len):
    model = Sequential()
    model.add(LSTM(
        512,
        input_shape=(network_input.shape[1], network_input.shape[2]),
        recurrent_dropout=0.3,
        return_sequences=True
    ))
    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
    model.add(LSTM(512))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(notes_len))
    model.add(Activation('softmax'))
    #model.compile(loss='categorical_crossentropy', optimizer='adam')
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    # Load the weights to each node
    #model.load_weights('weights-bach-adam.hdf5')
    model.load_weights('weights_classical_test.hdf5')
    return model

# PREDICTED_NOTES
# Function that predicts notes given a trained model
def predicted_notes(model, network_input, pitchnames, notes_len):
    # Choose random sequence used for prediction using trained model
    start = numpy.random.randint(0, len(network_input)-1)
    int_to_note = dict((number, note) for number, note in enumerate(pitchnames))
    pattern = network_input[start]
    prediction_output = []

    # Generate 500 notes
    for note_index in range(500):
        prediction_input = numpy.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(notes_len)

        # Use the trained model to predict notes
        prediction = model.predict(prediction_input, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]

    return prediction_output

# TODO: Instead of calling those here, import file and call functions in main
# Use the generate function to get an ML generated music file as output
generate()
