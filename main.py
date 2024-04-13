import argparse
from data_handling import load_data, filter_verbs
from text_processing import load_nlp_model, process_text
from advanced_text_processing import lemmatize_verbs, find_verb_locations, adjust_verb_locations
from rhyme_processing import replace_every_seventh_with_random_rhyme


def main():
    parser = argparse.ArgumentParser(
        description="Oulipo Variations: Advanced text processing utilities.")
    parser.add_argument(
        '--load', type=str, help='Path to the JSON file with input data for loading and processing')
    parser.add_argument('--process', type=str,
                        help='Path to a text file to process')
    parser.add_argument('--lemmatize', action='store_true',
                        help='Apply lemmatization to processed text')
    parser.add_argument('--rhyme', action='store_true',
                        help='Replace every seventh word with a rhyme')

    args = parser.parse_args()

    if args.load:
        print("Loading data...")
        df = load_data(args.load)
        print("Filtering verbs...")
        verbs_df = filter_verbs(df)
        print(verbs_df.head())

    if args.process:
        print("Loading NLP model...")
        nlp_model = load_nlp_model()
        print(f"Processing text from {args.process}...")
        with open(args.process, 'r') as file:
            text = file.read()
        if args.lemmatize:
            print("Lemmatizing text...")
            verbs = process_text(text, nlp_model)
            lemmatized_verbs = lemmatize_verbs(nlp_model, verbs.values())
            verb_locations = find_verb_locations(verbs_df, lemmatized_verbs)
            adjusted_verbs = adjust_verb_locations(verbs_df, verb_locations)
            print("Lemmatized and adjusted verbs:")
            print(adjusted_verbs)
        else:
            processed_text = process_text(text, nlp_model)
            print("Processed Text Output:")
            print(processed_text)

    if args.rhyme:
        print("Replacing every seventh word with a rhyme...")
        transformed_text = replace_every_seventh_with_random_rhyme(text)
        print("Transformed Text:")
        print(transformed_text)


if __name__ == "__main__":
    main()