import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Displays France life expectancy over years from CSV file.
    """
    try:
        dataFrame = load("life_expectancy_years.csv")
    except Exception:
        raise Exception("Can't load the file.")

    years = dataFrame.columns[1:]
    year_x = years.astype(int)
    france = dataFrame[dataFrame["country"] == "France"]
    france_y = france[years].iloc[0].values

    plt.plot(year_x, france_y)
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
