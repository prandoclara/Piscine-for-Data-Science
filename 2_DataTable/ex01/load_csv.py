import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a .csv file, handle errors, print dimensions, and return the DataFrame.
    Return None if the path is bad, file not found, or data invalid.
    """
    if not isinstance(path, str):
        print("Bad format")
        return None
    if not os.path.isfile(path):
        print("Invalid parameter")
        return None
    ext = os.path.splitext(path)[1].lower()
    if ext != ".csv":
        print("Bad extension")
        return None
    if not os.access(path, os.R_OK):
        print("File is not readable")
        return None

    try:
        data = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        print("The file is empty or only contains headers.")
        return None
    except ValueError:
        print("Error while reading the CSV file.")
        return None

    if data.empty:
        print("DataFrame is empty")
        return None

    print("Loading dataset of dimensions ", data.shape)
    return data
