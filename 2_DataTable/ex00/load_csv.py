import pandas as pd
import os


def load(path: str) -> pd.DataFrame:

    if not isinstance(path, str):
        print("Bad format")
        return None
    if not os.path.isfile(path):
        print("Invalid paramater")
        return None
    ext = os.path.splitext(path)[1].lower()
    if ext not in (".csv") or not ext:
        print("Bad extension")
        return None
    if not os.access(path, os.R_OK):
        print("File is not readable")
        return None

    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError("can't open the file.")
    except pd.errors.EmptyDataError:
        raise Exception("The file is empty or only contains headers.")

    if data.empty:
        raise Exception("DataFrame is empty")

    print("Loading dataset of dimensions ", data.shape)
    return data
