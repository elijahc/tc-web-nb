import pandas as pd

def load_cohort_from_json(path):
    return pd.read_json(path,lines=True,orient='records')
