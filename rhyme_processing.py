# rhyme_processing.py

import requests
import random
import spacy


def fetch_random_rhyme(word):
    api_url = f"http://api.datamuse.com/words?rel_rhy={word}"
    response = requests.get(api_url)
    if response.status_code == 200 and response.json():
        rhymes = response.json()
        random_rhyme = random.choice(rhymes)['word'].upper()
        return random_rhyme + " "
    return word.upper() + " "


def replace_every_seventh_with_random_rhyme(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    transformed_words = []
    for i, token in enumerate(doc):
        if token.is_alpha and (i + 1) % 7 == 0:
            rhyme = fetch_random_rhyme(token.text)
            transformed_words.append(rhyme)
        else:
            transformed_words.append(token.text_with_ws)
    return ''.join(transformed_words)
