# text_processing.py

import spacy
import string


def load_nlp_model(model_name="en_core_web_sm"):
    return spacy.load(model_name)


def process_text(text, nlp_model):
    text_without_punctuation = text.translate(
        str.maketrans('', '', string.punctuation))
    words = text_without_punctuation.split()
    verb_indices = {}
    for index, word in enumerate(words):
        doc = nlp_model(word)
        if doc[0].pos_ == 'VERB':
            verb_indices[index] = word
    return verb_indices
