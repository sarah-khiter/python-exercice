import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

def clean_population(population):
    cleaned_population = ''.join(filter(str.isdigit, population))
    if cleaned_population:
        return int(cleaned_population)
    else:
        return None

def scrape_site(url):
    html = get_html(url)
    
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extracting data from the table
        rows = soup.select('table tr')
        
        # Create lists to store data
        countries = []
        populations = []

        for row in rows[1:]:  # Skipping the header row
            cols = row.find_all('td')
            
            if len(cols) >= 3:  # Ensure that there are at least 3 columns
                country = cols[1].text.strip()
                population = clean_population(cols[2].text.strip())

                countries.append(country)
                populations.append(population)

        # Create a DataFrame
        df = pd.DataFrame({'Country': countries, 'Population': populations})

        # Trier les données par population en ordre décroissant
        df_sorted = df.sort_values(by='Population', ascending=False)

        # Save the sorted DataFrame to a CSV file
        df_sorted.to_csv('countries_population_sorted.csv', index=False)

        # Créer un graphique à barres
        plt.figure(figsize=(12, 6))
        plt.bar(df_sorted['Country'], df_sorted['Population'], color='skyblue')
        plt.title('Population des pays - Classement')
        plt.xlabel('Pays')
        plt.ylabel('Population')
        plt.xticks(df_sorted['Country'][::5], rotation=90)  # Afficher chaque cinquième étiquette
        plt.tight_layout()

        # Afficher le graphique
        plt.show()

def main():
    # URL du site à scraper
    site_url = "https://fr.vikidia.org/wiki/Liste_des_pays_par_population"
    
    # Exécutez la fonction de scraping
    scrape_site(site_url)

if __name__ == "__main__":
    main()
