from load_csv import load
import matplotlib.pyplot as plt


def convert_value(value: str) -> float:
    """
    converts a population expressed in k, M or B into a float number.
    Args:
        Value: a string expressing a population value in k, M or B.
    Returns:
        the population value expressed in float.
    """
    if value.endswith('k'):
        return float(value[:-1]) / 1000
    elif value.endswith('M'):
        return float(value[:-1])
    elif value.endswith('B'):
        return float(value[:-1]) * 1000
    else:
        return float(value)


def visualize_pop(pop_data, my_campus, country_choice):
    """
    displays population evolution from 1800 to 2050.
    Args:
        pop_data (data frame): dataset with population by country and by date.
        my_campus (str): country name of my campus.
        country_choice (str): country name of my choice.
    """
    delete_cols = [col for col in pop_data.columns
                   if col.isdigit() and int(col) >= 2051]
    pop_data.drop(delete_cols, axis=1, inplace=True)
    # axis=1 est utilisé pour supprimer des colonnes sinon axis=0
    # inplace=True modifie le pop_data original, False retourne une copie

    years = [int(year) for year in pop_data.columns[1:]]

    my_campus_data = pop_data[pop_data['country'] == my_campus]
    pop_my_campus_raw = my_campus_data.iloc[0, 1:].values
    pop_my_campus = [convert_value(pop) for pop in pop_my_campus_raw]

    country_choice_data = pop_data[pop_data['country'] == country_choice]
    pop_country_choice_raw = country_choice_data.iloc[0, 1:].values
    pop_country_choice = [convert_value(pop) for pop in pop_country_choice_raw]

    plt.figure(figsize=(7, 5))
    plt.plot(years, pop_my_campus, label=my_campus, color="green")
    plt.plot(years, pop_country_choice, label=country_choice, color="blue")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks([year for year in years if year % 40 == 0])
    min_year = min(years) - 10
    max_year = max(years) + 10
    plt.xlim(min_year, max_year)

    min_pop = min(min(pop_country_choice), min(pop_my_campus)) - 4
    max_pop = max(max(pop_country_choice), max(pop_my_campus)) + 4
    plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
    plt.ylim(min_pop, max_pop)

    plt.legend(loc='lower right')
    plt.show()


def main():
    try:
        df = load("population_total.csv")
        if df is None:
            return
        my_campus = 'France'
        country_choice = 'Germany'
        visualize_pop(df, my_campus, country_choice)

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()
