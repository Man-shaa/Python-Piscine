import sys
import pandas as pd
from typing import Union


def load(path: str) -> Union[pd.DataFrame, None]:
    """Load a CSV file from the specified path using pandas and return\
    it as a DataFrame."""
    dataset = pd.read_csv(path)
    return (dataset)

def main():
    try:
        if (len(sys.argv) != 2):
            raise ValueError("tuto: python load_csv.py [path]")
        path = sys.argv[1]
        print(load(path))
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)


if __name__ == "__main__":
    main()
