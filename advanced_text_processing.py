# advanced_text_processing.py

import spacy


def lemmatize_verbs(nlp_model, verbs):
    lemmatized_verbs = {}
    for verb in verbs:
        doc = nlp_model(verb)
        lemmatized_verbs[verb] = doc[0].lemma_.upper()
    return lemmatized_verbs


def find_verb_locations(verbs_df, lemmatized_verbs):
    lemmatized_verb_locations = {}
    for verb, lemmatized_verb in lemmatized_verbs.items():
        indices = verbs_df.index[verbs_df['word'] == lemmatized_verb].tolist()
        if indices:
            lemmatized_verb_locations[lemmatized_verb] = indices[0]
    return lemmatized_verb_locations


def adjust_verb_locations(verbs_df, verb_locations):
    new_verbs_list = {}
    for verb, location in verb_locations.items():
        new_index = location + 7
        try:
            new_verb = verbs_df.loc[new_index, 'word']
            new_verbs_list[verb] = new_verb
        except KeyError:
            continue
    return new_verbs_list
