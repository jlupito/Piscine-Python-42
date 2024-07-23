from load_csv import load
import matplotlib.pyplot as plt

def convert_value(value):
    """

    convert_value(value) -> float
    takes a population value expressed in k, M or B 
    and returns a population expressed in float

    """
    if value.endswith('k'):
        return float(value[:-1]) / 1000
    elif value.endswith('M'):
        return float(value[:-1])
    elif value.endswith('B'):
        return float(value[:-1]) * 1000
    else:
        return float(value)

def main():
    df = load("population_total.csv")
    if df is None:
        return
    
    delete_cols = [col for col in df.columns if col.isdigit() and int(col) >= 2051]
    df.drop(delete_cols, axis=1, inplace=True)
    # axis=1 est utilisé pour supprimer des colonnes sinon axis=0
    # inplace=True modifie le df original si inplace=False retourne une copie
    years = [int(year) for year in df.columns[1:]]
    france = df[df['country'] == 'France']
    belgium = df[df['country'] == 'Belgium']

    pop_fr = france.iloc[0, 1:].values
    pop_be = belgium.iloc[0, 1:].values

    converted_fr= [convert_value(pop) for pop in pop_fr]
    converted_be= [convert_value(pop) for pop in pop_be]

    plt.figure(figsize=(7, 5))
    plt.plot(years, converted_fr, label="France", color="green")
    plt.plot(years, converted_be, label="Belgium", color="blue")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks([year for year in years if year % 40 == 0])
    min_year = min(years) - 10
    max_year = max(years) + 10
    plt.xlim(min_year, max_year)

    min_pop = min(min(converted_be) ,min(converted_fr)) - 4
    max_pop = max(max(converted_be) ,max(converted_fr)) + 4
    plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
    plt.ylim(min_pop, max_pop)

    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    main()