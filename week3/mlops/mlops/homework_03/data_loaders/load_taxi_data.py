import requests
from io import BytesIO
from typing import List

import pandas as pd


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:

    response = requests.get(
               "https://github.com/remitoudic/mlops/raw/main/week3/datasets/yellow/2023/03.parquet"
            )

    if response.status_code != 200:
        raise Exception(response.text)

    df = pd.read_parquet(BytesIO(response.content))
    
    return df
