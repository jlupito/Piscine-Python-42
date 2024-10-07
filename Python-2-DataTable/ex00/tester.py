from load_csv import load


def main():
    life_expectancy = load("life_expectancy_years.csv")
    if life_expectancy is None:
        return
    print(life_expectancy.head(5))


if __name__ == "__main__":
    main()
