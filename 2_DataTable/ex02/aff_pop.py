import matplotlib.pyplot as plt
from load_csv import load


def convert_pop_value(x):
    """
    Converts strings like '3.2M' or '400k' to float values.
    """
    if isinstance(x, str):
        x = x.strip()
        if x.endswith('M'):
            return float(x[:-1]) * 1_000_000
        elif x.endswith('k'):
            return float(x[:-1]) * 1_000
        elif x == '' or x.lower() == 'nan':
            return None
        else:
            try:
                return float(x)
            except ValueError:
                return None
    return x


def main():
    """
    Compares France and Belgium population growth from CSV file.
    """
    try:
        df = load("population_total.csv")
    except Exception:
        raise Exception("Can't load the file.")

    years = df.columns[1:]
    year_x = years.astype(int)

    for col in df.columns[1:]:
        df[col] = df[col].apply(convert_pop_value)

    france = df[df["country"] == "France"]
    france_pop = france[years].iloc[0].values

    belgium = df[df["country"] == "Belgium"]
    belgium_pop = belgium[years].iloc[0].values

    plt.plot(year_x, france_pop, label="France")
    plt.plot(year_x, belgium_pop, label="Belgium")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.xlim(1800, 2050)
    plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.show()


if __name__ == "__main__":
    main()
