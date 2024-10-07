from load_csv import load
import matplotlib.pyplot as plt


def visualize_pop(data_life, my_country):
    """
    displays life expectancy evolution from 1800 to 2050.
    Args:
        data_life (data frame): dataset with life expectancy
        by country and by date.
        my_campus (str): country name of my campus.
        country_choice (str): country name of my choice.
    """
    try:
        # on extraie les annees des colonnes du df a partir
        # de la premiere colonne:
        years = [int(year) for year in data_life.columns[1:]]

        # on filtre pour avoir les donnees de la france:
        country = data_life[data_life['country'] == my_country]

        # on extraie les donnees de l esperance de vie pour la france
        # a partir de la premiere colonne:
        life_exp = country.iloc[0, 1:].values

        plt.figure(figsize=(8, 5))
        plt.plot(years, life_exp)
        plt.title(f"{my_country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks([year for year in years if year % 40 == 0])
        plt.show()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


def main():
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            return
        country = 'France'
        visualize_pop(df, country)

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()
