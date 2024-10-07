from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
# import traceback


def visualize_life_gnp(income_data, life_data, date):
    try:
        if date not in income_data.columns or date not in life_data.columns:
            raise AssertionError(f"Date {date} is not valid.")

        income = income_data[['country', date]].rename(columns={date:
                                                                'income'})
        life = life_data[['country', date]].rename(columns={date:
                                                            'life_expectancy'})
        merged_data = pd.merge(income, life, on='country')

        plt.figure(figsize=(10, 6))
        plt.scatter(merged_data['income'], merged_data['life_expectancy'],
                    alpha=0.5, marker='o', color='b')
        plt.title(date)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.show()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        # traceback.print_exc()
        return


def main():
    try:
        df_income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df_life = load("life_expectancy_years.csv")
        if df_income is None or df_life is None:
            return
        date = '1400'
        visualize_life_gnp(df_income, df_life, date)

    except Exception as e:
        print(type(e).__name__ + ":", e)
        # traceback.print_exc()
        return


if __name__ == "__main__":
    main()
