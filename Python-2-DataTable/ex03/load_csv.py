import pandas as pd

def load(path: str) -> pd.DataFrame:
    """
    load(path: str) -> pd.DataFrame
    takes a path as argument, writes the dimensions of the data set
    and returns it.
    """

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: File could not be parsed. Please check the file format.")
        return None
    except PermissionError:
        print("Error: Permission denied. You do not have the necessary permissions for the file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None