import requests
from bs4 import BeautifulSoup
import json

# List of sources to scrape
sources = [
    'https://krebsonsecurity.com/',
    'https://thehackernews.com/',
    'https://www.darkreading.com/',
    'https://www.securityweek.com/',
    'https://www.bleepingcomputer.com/',
    # Add more sources as needed...
]

def scrape_news():
    news = []
    for url in sources:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example of extracting news articles (modify based on each site's structure)
            for article in soup.find_all('article'):
                title = article.find('h2').get_text()
                description = article.find('p').get_text() if article.find('p') else "No description available"
                link = article.find('a')['href']
                news.append({
                    'title': title,
                    'description': description,
                    'link': link,
                    'source': url
                })
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    # Save the news to a JSON file
    with open('news_data.json', 'w') as f:
        json.dump(news, f, indent=4)
        

if __name__ == "__main__":
    scrape_news()
