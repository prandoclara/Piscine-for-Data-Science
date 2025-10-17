import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
  Displays life expectancy vs GDP per capita for year 1900.
    """
    try:
        df_pib = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df_life = load("life_expectancy_years.csv")
    except Exception:
        raise Exception("Can't load one or both files")

    pib_year_1900 = df_pib['1900']
    life_year_1900 = df_life['1900']

    plt.scatter(pib_year_1900, life_year_1900)
    plt.title("1900")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
