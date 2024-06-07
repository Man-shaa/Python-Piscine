import sys
from load_csv import load
import matplotlib.pyplot as plt


def aff_life(data_set):
    """Plot the life expectancy over the years for a given dataset filtered\
    by country name."""
    campus_data = data_set[data_set['country'] == "France"]
    plt.plot(campus_data.columns[1:], campus_data.iloc[0, 1:])
    plt.title("Life Expectancy Over the Years for Your Campus")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (years)")
    plt.legend(["Your Campus"])
    # plt.grid(True)
    plt.xticks(campus_data.columns[1::40])

    plt.show()


def main():
    try:
        if (len(sys.argv) != 2):
            raise ValueError("tuto: python aff_life.py [path]")
        data_set = load(sys.argv[1])
        aff_life(data_set)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)


if __name__ == "__main__":
    main()
