import pandas as pd
import os

from requests import get
from country_viz import c

def download_data(url: str=c['DATA']['DATASET_URL']) -> None:
    """
    Downloads the raw data
    url : url of the file to download
    """
    try:
        r = get(url)
        with open(os.path.join(c['DATA']['RAW_DATA_PATH'], c['DATA']['DATASET_RAW_NAME']), mode="wb") as file:
            file.write(r.content)
    except Exception as error: print(f"Download data failure : {error}")

def clean_data() -> None:
    """
    Clean the data
    """

    df = pd.read_csv(os.path.join(c['DATA']['RAW_DATA_PATH'], c['DATA']['DATASET_FILENAME']),
                    sep=';',
                    skiprows=3,
                    quotechar='#',
                    decimal=',',
                    usecols=c['DATA']['DATASET_DTYPES'].keys(),
                    dtype=c['DATA']['DATASET_DTYPES'],
                    )
    df.to_csv(os.path.join(c['DATA']['PROCESSED_DATA_PATH'],
                           c['DATA']['CLEAN_DATASET_NAME'],
                           index=False))