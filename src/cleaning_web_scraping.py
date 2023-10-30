import pandas as pd
from src import web_scraping
#from src import visualization



def cleaning_continent_df():
    web_scraping.webscraping_data()
    df_country_africa = pd.read_csv("./Data/Unprocessed_data/Weather_continent/df_country_africa.csv" , sep= ",",encoding= 'utf-8')
    df_country_asia = pd.read_csv("./Data/Unprocessed_data/Weather_continent/df_country_asia.csv" , sep= ",",encoding= 'utf-8')
    df_country_europe = pd.read_csv("./Data/Unprocessed_data/Weather_continent/df_country_europe.csv" , sep= ",",encoding= 'utf-8')
    df_country_north_america = pd.read_csv("./Data/Unprocessed_data/Weather_continent/df_country_north_america.csv" , sep= ",",encoding= 'utf-8')
    df_country_oceania = pd.read_csv("./Data/Unprocessed_data/Weather_continent/df_country_oceania.csv" , sep= ",",encoding= 'utf-8')
    df_country_south_america=pd.read_csv("./Data/Unprocessed_data/Weather_continent/df_country_south_america.csv" , sep= ",",encoding= 'utf-8')

    dataframes = [
        df_country_africa,
        df_country_asia,
        df_country_europe,
        df_country_north_america,
        df_country_oceania,
        df_country_south_america
    ]
    def drop_ref_column(df):
        df.drop(columns=["Ref."], inplace=True)
    for df in dataframes:
        drop_ref_column(df)

    #Adding the continents to each df
    continent_names = [
        'Africa',
        'Asia',
        'Europe',
        'North America',
        'Oceania',
        'South America'
    ]
    #merge all df of each continent
    for df, continent in zip(dataframes, continent_names):
        df.insert(0, 'Continent', continent)

    df_temp = pd.concat(dataframes, ignore_index=True)

    # List of month and Year columns
    temp_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Year']

    # Extract Celsius temperatures and convert to float
    for col in temp_columns:
        df_temp[col] = df_temp[col].str.extract('([0-9.]+)').astype(float)
    
    return df_temp