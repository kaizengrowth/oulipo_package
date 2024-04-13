import spacy
import random

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


def shuffle_every_other_word_and_rotate(text):
    # Parse the text
    doc = nlp(text)

    # Extract words as strings, preserving whitespace
    words = [token.text_with_ws for token in doc]

    # Initialize a list to store each variation after shuffling
    variations = []

    # Set the initial starting index for shuffling to 1 (i.e., the second word)
    start_index = 1

    # Repeat the shuffling process 7 times
    for iteration in range(7):
        # Shuffle every other word starting from 'start_index'
        for i in range(start_index, len(words), 2):
            # Random step within range
            shift = random.randint(1, len(words) - 2)
            # Calculate new position with wrap-around
            new_position = (i + shift) % len(words)

            # Swap the current word with the word at the new position
            words[i], words[new_position] = words[new_position], words[i]

        # After each shuffle, add the current variation to the list
        current_variation = "".join(words).strip()
        variations.append(current_variation)

        # Rotate the starting index for shuffling (alternate between 1 and 0)
        # This toggles the starting index between 1 and 0
        start_index = (start_index + 1) % 2

    return variations
