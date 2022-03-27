# This file contains various functions with recurrent use

from music21 import *
import pickle
import glob

# PARSE_MIDI
# Function to parse through midi files in given path
def parse_midi(path):
    notes = []
    # Choose whether or not to have rests in the data
    rest = False
    for file in glob.glob(path + "/*.mid"):
        print("Working on: \n",file)
        notes_in_file = None
        midi = converter.parse(file)

        try: 
            # Partition instruments
            instruments = instrument.partitionByInstrument(midi)
            notes_to_parse = instruments.parts[0].recurse()
        except: 
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            # Note
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            # Chord
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
            # Rest
            elif isinstance(element, note.Rest) and rest:
                notes.append("rest")
    
    # Create a file containing the notes parsed
    with open('data/notes_parsed/notes_', 'wb') as fp:
        pickle.dump(notes, fp)

    # Return array with notes
    return notes

# ADD_SEMITONES
# Increase notes in note_array by nr_semitones
def add_semitones(note_array, nr_semitones):
    increased_notes = []
    for notes in note_array:
        # Chord Case
        if ('.' in notes) or notes.isdigit():
            chord_notes = notes.split('.')
            new_notes = []
            for current_note in chord_notes:
                increased_note = (pitch.Pitch(int(current_note)).transpose(nr_semitones))
                new_notes.append(increased_note)
            new_chord = chord.Chord(new_notes)
            increased_notes.append('.'.join(str(n) for n in new_chord.normalOrder))
        # Rest case
        elif notes == 'rest':
            increased_notes.append("rest")
        # Note case
        else:
            increased_note = (pitch.Pitch(notes).transpose(nr_semitones))
            increased_notes.append(str(increased_note))

    return increased_notes


# OUTPUT_MIDI
# Create midi file of given predicted notes array
def output_midi(prediction_output, file_name):
    print("Converting to MIDI \n")
    offset = 0
    output_notes = []

    # Create notes, chords and rests depending on the 
    for notes in prediction_output:
        # Chord 
        if ('.' in notes) or notes.isdigit():
            notes_in_chord = notes.split('.')
            new_notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                new_notes.append(new_note)
                
            new_chord = chord.Chord(new_notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        # Rest
        elif notes == 'rest':
            new_note = note.Rest()
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)    
        # Note
        else:
            new_note = note.Note(notes)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        # Make sure notes don't stack by increasing offset
        offset += 0.5
    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp=("results/" + file_name + '_result.mid'))
