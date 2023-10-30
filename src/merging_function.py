import pandas as pd

def merge_michelin_and_temp(df_michelin, df_temp_continents):
    # First, merge based on 'Country'
    intermediate_df = pd.merge(df_michelin, df_temp_continents, how='inner', on='Country')
    
    # Then, filter this intermediate dataframe based on the 'City'
    df_Michelin_temp = intermediate_df[intermediate_df['City_x'] == intermediate_df['City_y']]
    
    # Keep only the relevant columns if needed
    relevant_columns = ['Name', 'Price', 'Cuisine', 'Award', 'FacilitiesAndServices',
                        'Description', 'Combined', 'City_x', 'Country', 'Continent',
                        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                        'Sep', 'Oct', 'Nov', 'Dec', 'Year']
    df_Michelin_temp = df_Michelin_temp[relevant_columns]
    
    # Rename the 'City_x' column back to 'City'
    df_Michelin_temp.rename(columns={'City_x': 'City'}, inplace=True)
    
    return df_Michelin_temp

