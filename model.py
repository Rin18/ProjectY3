""" 
Code was heavily inspired by the following tutorial:
https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5
"""
# This file contains the lstm model used to generate music

from functions import *
from keras.layers import BatchNormalization as BatchNorm
from keras.layers import Activation
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.utils import np_utils
import numpy

# GET_MODEL
# Function that, given parsed notes as argument, trains the model
def get_model(notes):
    # Length of notes set
    notes_len = len(set(notes))
    # Create network input
    network_input, network_output = get_input(notes, notes_len)
    # Create model
    model = create_network(network_input, notes_len)
    # Start training the model
    train_model(model, network_input, network_output)

# GET_INPUT
# Function that, given parsed notes as argument, shapes them as input and output for model
def get_input(notes, notes_len):
    # Pitch names from notes set
    pitchnames = sorted(set(item for item in notes))
    # Note to integer map
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

    # To predict the next note, we take into account the previous 100 notes.
    # Increase to 250 and see what happens
    sequence_length = 100
    network_input = []
    network_output = []
    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])
        network_output.append(note_to_int[sequence_out])

     # Innput is incompatible with LSTM layers, fix that
    n_patterns = len(network_input)
    network_input = numpy.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(notes_len)
    network_output = np_utils.to_categorical(network_output)
    return (network_input, network_output)

# CREATE_NETWORK
# Function for creating the LSTM neural network
# Contains three LSTM layers, three Dropout layers, 
# two Dense layers and two activation layers
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
    # Try sparse categorical cross entropy and adam/nadam and see if performance improves
    # It should improve memory and computation performance as sparse doesnt use vectors
    # Should take less to train and it will be interesting to see how the model performs with the change
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model

# TRAIN_MODEL
# Function for training the LSTM neural network
def train_model(model, network_input, network_output):
    # After each epoch, save the weights
    filepath = "training_models/weights-bach-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )

    # loading saved model and start training from last checkpoint
    model.load_weights('weights-bach-05.hdf5')
    callbacks_list = [checkpoint]
    model.fit(network_input, network_output, epochs=20, batch_size=128, callbacks=callbacks_list)

# TODO: Instead of calling those here, import file and call functions in main
# Train model with already parsed notes
note_path = 'data/notes_parsed/notes_bach'
with open(note_path, 'rb') as filepath:
    notes = pickle.load(filepath)
print("Using: \n", note_path)
get_model(notes)
