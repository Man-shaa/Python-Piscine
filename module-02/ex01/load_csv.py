import sys
import pandas as pd
from typing import Union


def load(path: str) -> Union[pd.DataFrame, None]:
    """Load a CSV file from the specified path using pandas and return it as\
    a DataFrame.
    If the file cannot be loaded, return None."""
    try:
        dataset = pd.read_csv(path)
        return (dataset)
    except Exception as e:
        raise FileNotFoundError("Failed to load path : {e}", e)


def main():
    if (len(sys.argv) != 2):
        raise ValueError("tuto: python load_csv.py [path]")
    path = sys.argv[1]
    print(load(path))


if __name__ == "__main__":
    main()
