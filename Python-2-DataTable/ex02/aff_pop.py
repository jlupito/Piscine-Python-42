from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        return
    years = [int(year) for year in df.columns[1:]]
    france = df[df['country'] == 'France']
    belgium = df[df['country'] == 'Belgium']
    life_exp = france.iloc[0, 1:].values
    plt.figure(figsize=(8, 5))
    plt.plot(years, life_exp, )
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks([year for year in years if year % 40 == 0])
    plt.show()

if __name__ == "__main__":
    main()