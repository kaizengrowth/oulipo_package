from music21 import stream, note
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


def get_every_seventh_character(text):
    # Select every seventh character from the text
    return [char for i, char in enumerate(text) if (i + 1) % 7 == 0 and char.isalpha()]


def char_to_pitch(char):
    # Map the character's position in the alphabet to a MIDI pitch
    base_note = 60  # Middle C
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_position = alphabet.index(
        char.lower()) if char.lower() in alphabet else 0
    # Keep within an octave for simplicity
    return base_note + (char_position % 12)


def create_music_with_music21(chars):
    # Create a music21 stream to hold the music
    part = stream.Part()
    for char in chars:
        # Use the char_to_pitch function to determine the pitch
        # Convert character position to MIDI pitch
        midi_pitch = char_to_pitch(char)
        new_note = note.Note(midi_pitch)
        new_note.duration.type = 'quarter'  # Set note duration to a quarter note
        part.append(new_note)

    # Show the music as MIDI
    part.show('midi')
