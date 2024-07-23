from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    df_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")
    if df_income is None or df_life is None:
        return
    
    date = '1900'

    income = df_income[['country', date]].rename(columns={date: 'income'})
    life = df_life[['country', date]].rename(columns={date: 'life_expectancy'})

    merged_data = pd.merge(income, life, on='country')

    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['income'], merged_data['life_expectancy'], alpha=0.5, marker='o', color='b')
    plt.title(date)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()

if __name__ == "__main__":
    main()