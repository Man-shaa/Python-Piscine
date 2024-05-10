import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def convert_population(population):
    """
    this fonction handle the way the population is displayed
    """
    if population.endswith("M"):
        return float(population[:-1]) * 1_000_000
    elif population.endswith("k"):
        return float(population[:-1]) * 1_000
    else:
        return float(population)


def millions_formatter(x, pos):
    """
    this functions formatte the number on the scale
        For example, if x is 1500000,
        the function will return the string "1M".
    """
    return f'{x / 1e6:.0f}M'


def aff_pop(population):
    country1 = "France"
    country2 = "Belgium"

    first_data_set = population[population['country'] == country1].\
        drop('country', axis=1).T
    second_data_set = population[population['country'] == country2].\
        drop('country', axis=1).T

    first_data_set = first_data_set.loc['1800':'2050']
    second_data_set = second_data_set.loc['1800':'2050']

    first_data_set = first_data_set.squeeze().apply(convert_population)
    second_data_set = second_data_set.squeeze().apply(convert_population)

    plt.plot(first_data_set, label=country1)
    plt.plot(second_data_set, label=country2)

    x_ticks = first_data_set.index[::40]
    plt.xticks(x_ticks)

    plt.title("Population Comparison between Your Campus and Other Country")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    max_population = FuncFormatter(millions_formatter)
    plt.gca().yaxis.set_major_formatter(max_population)

    plt.show()


def main():
    if (len(sys.argv) != 2):
        raise ValueError("tuto: python aff_pop.py [path]")
    population_set = load(sys.argv[1])
    aff_pop(population_set)


if __name__ == "__main__":
    main()
