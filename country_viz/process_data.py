
import pandas as pd
import os

from country_viz import c

def process_data(df: pd.DataFrame) -> None:
    """
    Load and process the data
    """

    df = pd.read_csv(os.path.join(c['DATA']['PROCESSED_DATA_PATH'],
                                c['DATA']['PROCESSED_DATASET_FILENAME']),
                                dtype=c['DATA']['DATASET_DTYPES'])

    df['density (km²)'] = df['population'] / df['area (km²)']

    df.to_csv(os.path.join(c['DATA']['PROCESSED_DATA_PATH'],
                            c['DATA']['PROCESSED_DATASET_NAME'],
                            index=False))