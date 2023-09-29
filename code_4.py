import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}')"
    df_by_date = df.query(query)
    mean_dollar_price = df_by_date['dollar_price'].mean()
    return round(mean_dollar_price,2)

def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3 == '{country_code.upper()}')"
    df_by_date = df.query(query)
    mean_dollar_price = df_by_date['dollar_price'].mean()
    return round(mean_dollar_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_by_min = df.query(query)
    min_query = df_by_min['dollar_price'].idxmin()
    cheapest = round(df_by_min.loc[min_query]['dollar_price'],2)
    row = df_by_min.loc[min_query]
    name = row['name']
    country_code = row['iso_a3']
    return f"{name}({country_code}): ${cheapest}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_by_max = df.query(query)
    max_query = df_by_max['dollar_price'].idxmax()
    expensive = round(df_by_max.loc[max_query]['dollar_price'],2)
    row = df_by_max.loc[max_query]
    name = row['name']
    country_code = row['iso_a3']
    return f"{name}({country_code}): ${expensive}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)