from load_csv import load
import matplotlib.pyplot as plt


def draw_projection_for_year(data, life_expectancy_data, year: str):
    """Draw a scatter plot of life expectancy vs GNP per capita for a\
    given year."""
    if data is not None and life_expectancy_data is not None:
        gnp_year = data[['country', year]]
        life_exp_year = life_expectancy_data[['country', year]]
        merged_data = gnp_year.merge(life_exp_year, on='country', how='inner')
        merged_data.columns = ['Country', 'GNP', 'Life Expectancy']

        plt.figure(figsize=(10, 6))
        plt.scatter(merged_data['GNP'], merged_data['Life Expectancy'])

        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.xscale('log')
        plt.xticks([1000, 10000], ['1k', '10k'])
        plt.ylabel('Life Expectancy')

        plt.show()

    else:
        print("Unable to load one or both datasets.")


def main():
    try:
        file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        data = load(file)
        if (data is None):
            raise ValueError("Unable to load income_[...].csv")

        life_expectancy_data = load("life_expectancy_years.csv")
        if (life_expectancy_data is None):
            raise ValueError("Unable to load life_expectancy_years.csv")
        draw_projection_for_year(data, life_expectancy_data, '1900')
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)


if __name__ == "__main__":
    main()
