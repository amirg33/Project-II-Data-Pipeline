import pandas as pd

def webscraping_data():
    url = "https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature"

    #Save all the tables in the weather Continent folder as a .csv file
    df_country_africa = pd.read_html(url)[0]
    df_country_africa.to_csv("Data/Unprocessed_data/Weather_continent/df_country_africa.csv", index=False)
    df_country_asia = pd.read_html(url)[1]
    df_country_asia.to_csv("Data/Unprocessed_data/Weather_continent/df_country_asia.csv", index=False)
    df_country_europe = pd.read_html(url)[2]
    df_country_europe.to_csv("Data/Unprocessed_data/Weather_continent/df_country_europe.csv", index=False)
    df_country_north_america = pd.read_html(url)[3]
    df_country_north_america.to_csv("Data/Unprocessed_data/Weather_continent/df_country_north_america.csv", index=False)
    df_country_oceania = pd.read_html(url)[4]
    df_country_oceania.to_csv("Data/Unprocessed_data/Weather_continent/df_country_oceania.csv", index=False)
    df_country_south_america = pd.read_html(url)[5]
    df_country_south_america.to_csv("Data/Unprocessed_data/Weather_continent/df_country_south_america.csv", index=False)