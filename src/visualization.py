import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualization(df):
# Counting the frequency of each award type
    award_count = df['Award'].value_counts()

    # Plotting
    plt.figure(figsize=(14, 7))
    sns.barplot(x=award_count.index, y=award_count.values)
    plt.title('Frequency of Different Award Types')
    plt.xlabel('Award Type')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()

    ## ____________________

    # Count the number of awards for each city and sort them
    city_award_count = df.groupby('City')['Award'].count().sort_values(ascending=False)
    top_cities = city_award_count.head(10)  # Get top 10 cities by award count

    # Plotting top cities by award count
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_cities.index, y=top_cities.values)
    plt.title('Top 10 Cities by Award Count')
    plt.xlabel('City')
    plt.ylabel('Number of Awards')
    plt.xticks(rotation=45)
    plt.show()

## ____________________

    # For each top city, list and visualize the types of awards
    for city in top_cities.index:
        plt.figure(figsize=(12, 6))
        city_awards = df[df['City'] == city]['Award'].value_counts()
        sns.barplot(x=city_awards.index, y=city_awards.values)
        plt.title(f'Types of Awards in {city}')
        plt.xlabel('Award Type')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()

## ____________________


    # Count the number of awards for each city and sort them
    city_award_count = df.groupby('City')['Award'].count().sort_values(ascending=False)
    top_cities = city_award_count.head(7)  # Get top 7 cities by award count

    # Create an empty DataFrame to store award frequencies for each top city
    award_data = pd.DataFrame()

    # For each top city, get the types and frequencies of awards
    for city in top_cities.index:
        city_awards = df[df['City'] == city]['Award'].value_counts().reset_index()
        city_awards.columns = ['Award', 'Frequency']
        city_awards['City'] = city
        award_data = pd.concat([award_data, city_awards])

    # Create the grouped bar chart
    plt.figure(figsize=(16, 8))
    sns.barplot(x='City', y='Frequency', hue='Award', data=award_data)
    plt.title('Types of Awards in Top 7 Cities')
    plt.xlabel('City')
    plt.ylabel('Frequency')
    plt.legend(title='Award Types', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
