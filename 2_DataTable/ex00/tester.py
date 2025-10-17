from load_csv import load

try:
    print(load("life_expectancy_years.csv"))
except FileNotFoundError as fnf:
    print("Caught Error: ", fnf)
except Exception as e:
    print("Caught Error: ", e)
