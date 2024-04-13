# data_handling.py

import pandas as pd
import json


def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)


def filter_verbs(dataframe):
    verbs_df = dataframe[dataframe['pos'] == 'v.']
    return verbs_df.reset_index(drop=True)
