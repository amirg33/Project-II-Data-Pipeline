import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt 
#import seaborn as sns
import re
#from geopy.geocoders import Nominatim
#from geopy.point import Point
from cProfile import label
def clean_csv():
    df = pd.read_csv("../Project-II-Data-Pipeline/Data/michelin_my_maps.csv",sep=',' ,encoding= 'utf-8')
    df.drop(columns=["Url","WebsiteUrl","PhoneNumber"], inplace=True)
    df['Combined'] = df['Latitude'].astype(str) + ', ' + df['Longitude'].astype(str)
    df.drop(columns=["Longitude","Latitude","Address"], inplace=True)
    #Correct the row's for awards
    awards_to_keep = ["1 Star MICHELIN", "2 Stars MICHELIN", "3 Stars MICHELIN", "Bib Gourmand", "MICHELIN Green Star"]
    # Filter the dataframe to keep only rows with those awards
    df = df[df['Award'].isin(awards_to_keep)]

    #geolocator = Nominatim(user_agent="test")

    #def reverse_geocoding(lat, lon):
    #    try:
    #        location = geolocator.reverse(Point(lat, lon))
    #        return location.raw['display_name']
    #    except:
    #        return None
    #df_sample = df.sample()
    #df_sample['address'] = np.vectorize(reverse_geocoding)(df['Latitude'], df['Longitude'])
    #df_sample['address']

    def replace_to_dollar_signs(price):
        if isinstance(price, str):
            unique_char = set(price)
            if len(unique_char) == 1:
                char = list(unique_char)[0]
                count = price.count(char)
                return '$' * count
        else:
            return price  # return the original value if it's not a string

    df['Price'] = df['Price'].apply(replace_to_dollar_signs)


    def standardize_country(location):
        if not isinstance(location, str):
            return 'Unknown'
        location = location.split(",")[-1].strip()
        
        # Comprehensive list of countries for standardization
        common_countries = [
            ('USA', ['USA', 'United States', 'United States of America']),
            ('UK', ['UK', 'United Kingdom', 'England']),
            ('France', ['France']),
            ('Germany', ['Germany']),
            ('Spain', ['Spain']),
            ('China', ['China', 'China Mainland', 'Hong Kong', 'Macau', 'Hong Kong SAR China']),
            ('United Arab Emirates', ['Dubai', 'Abu Dhabi']),
            ('Czech Republic', ['Czechia', 'Czech Republic']),
            ('Turkey', ['Türkiye']),
            ('Singapore', ['Singapore'])
            # Add more country names and their variants here
        ]
        
        for country_standard, country_variants in common_countries:
            for variant in country_variants:
                if variant == location:
                    return country_standard
        return location

    country_synonyms = {
        'United States': 'USA',
        'United States of America': 'USA',
        'United Kingdom': 'UK',
        'England': 'UK',
        'China Mainland': 'China',
        'Hong Kong': 'China',
        'Macau': 'China',
        'Hong Kong SAR China': 'China',
        'Dubai': 'United Arab Emirates',
        'Abu Dhabi': 'United Arab Emirates',
        'Czechia': 'Czech Republic',
        'Türkiye': 'Turkey'
    }

    def split_location(location):
        parts = location.split(", ")
        if len(parts) < 2:
            return location, "Unknown"  
        city = parts[0].strip()
        _ = None

        # Standardize country name using dictionary

        return city, _

    def hybrid_approach(location):
        city, _ = split_location(location)
        standardized_country = standardize_country(location)
        return city, standardized_country

    df['City'], df['Country'] = zip(*df['Location'].apply(hybrid_approach))
    df.drop(columns=["Location"], inplace=True)
    #df.to_csv("cleaned.csv", index=False)
    return df