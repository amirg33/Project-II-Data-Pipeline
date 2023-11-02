# Project-II-Data-Pipeline

# INTRODUCTION:

### Brief Overview:

- During this project I have looked at Michelin Star restaurants and their locations.
- The second idea was to donwload and some Web-Scraping about the average Weather in each city furing the year. 

### Where Did We Get Our Information?:
- Michelin star Restaurant: [LINK](https://github.com/ngshiheng/michelin-my-maps/blob/main/data/michelin_my_maps.csv)
- Average weather during the year: [LINK](https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature)

# Questions to be answered
### Primary Questions: 

- What relation does the weather have with Michelin star restaurants & spicy food?
### Secondary Questions:
- What kind of Michelin stars exist?
- Which are the countries / Cities that have the most?

#### Click [HERE](https://www.canva.com/design/DAFyv5alKQk/t0XpkC70am3L8LNokUAJnw/edit?utm_content=DAFyv5alKQk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) to go to the  presentation.

# Cleaning and Merging 🧹🤝
## Michelin Restaurant Data (michelin_my_maps.csv)
- **Drop Unnecessary Columns:** Columns like "Url", "WebsiteUrl", and "PhoneNumber" are dropped.

- **Create Combined Column:**: Combine "Latitude" and "Longitude" into a single column named "Combined".

- **Filter Awards:** Only rows with specific Michelin awards like 1, 2, 3 Stars, Bib Gourmand, and Green Star are kept.

- **Standardize Price:** The 'Price' column is standardized to use dollar signs instead of various currency symbols.

- **Split Location:** 'Location' is split into two new columns: City and Country. Country names are also standardized.

## Weather Data (Web-scraped from Wikipedia)
- **Load data:** Data is loaded into separate DataFrames for each continent.

- **Drop Ref. Column:** The reference column is dropped from each continent's DataFrame.

- **Add Continent Column** A new column indicating the continent is added to each DataFrame.

- **Merge DataFrames** All continent DataFrames are merged into a single DataFrame.

![Fusion](https://i.imgflip.com/10av7r.jpg)

- **Extract Temperatures** Temperature data in the columns for each month is extracted and converted to float.
  
## Merging Michelin and Weather Data
- **Country-Based Merge** The Michelin and weather data are first merged based on the 'Country' column.

![Ironman and CA handshake](https://qph.cf2.quoracdn.net/main-qimg-627096fec56168babb9a61ef6089017c-lq)

- **City-Based Filte** The merged DataFrame is filtered to match cities.

- **Select Relevant Columns** Only the relevant columns are kept in the merged DataFrame.
