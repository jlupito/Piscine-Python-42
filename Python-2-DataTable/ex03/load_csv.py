import pandas as pd
from os import access, R_OK


def load(path: str) -> pd.DataFrame:
    """
    takes a path as argument, writes the dimensions of the data set
    and returns it.

    Args:
        Path (str): path to the csv file to load.

    Returns:
        A pandas data set.
    """
    try:
        try:
            df = pd.read_csv(path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"{e}.")
        except pd.errors.EmptyDataError:
            print("Error: File is empty.")
            return None
        except pd.errors.ParserError:
            print("Error: File could not be parsed. \
                  Please check the file format.")
            return None
        except IOError:
            if not access(path, R_OK):
                print(f"The file '{path}' is not readable.")
            else:
                print(f"The file '{path}' is not a valid image file.")
            return None
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return
